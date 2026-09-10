// PassMaster AI — Master Client Engine (Mani$oft Edition)

let allQuestions = [];
let filteredQuestions = [];
let currentIndex = 0;
let sessionHistory = {};
let timerInterval = null;
let fullJambTimerInterval = null;
let timerSeconds = 40;
let examTimeRemaining = 7200; // 120 minutes for Full JAMB CBT
let cbtMode = 'drill'; // 'drill' or 'full_jamb'
let activePlan = null;
let currentUser = null;
let audioEnabled = true;
let sfxEnabled = true;
let flaggedQuestions = new Set();
let antiCheatSwitchCount = 0;
let syllabusData = null;
let loadedLessons = [];
let activeLessonData = null;
let currentActiveSubject = 'all';
let currentActiveTopic = 'all';

// Calculator state
let calcCurrent = "0";
let calcPrev = null;
let calcOp = null;

// Candidate Defaults
let candidateName = "Olive Tobi";
let targetCourse = "Medicine & Surgery";
let targetUni = "UNILAG";

// Web Audio Synthesis Context
let audioCtx = null;
function getAudioContext() {
  if (!audioCtx) {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (AudioContext) audioCtx = new AudioContext();
  }
  return audioCtx;
}

function playSound(type) {
  if (!sfxEnabled) return;
  try {
    const ctx = getAudioContext();
    if (!ctx) return;
    if (ctx.state === "suspended") ctx.resume();

    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);

    if (type === "correct") {
      // Pleasant victory chime
      osc.type = "triangle";
      osc.frequency.setValueAtTime(523.25, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(659.25, ctx.currentTime + 0.12);
      osc.frequency.exponentialRampToValueAtTime(783.99, ctx.currentTime + 0.25);
      gain.gain.setValueAtTime(0.2, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.4);
      osc.start();
      osc.stop(ctx.currentTime + 0.4);
    } else if (type === "wrong") {
      // Gentle warning buzz
      osc.type = "sawtooth";
      osc.frequency.setValueAtTime(220, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(140, ctx.currentTime + 0.2);
      gain.gain.setValueAtTime(0.2, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
      osc.start();
      osc.stop(ctx.currentTime + 0.3);
    }
  } catch (e) {
    console.log("Audio FX error", e);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  checkAuth();
  loadQuestions();
  loadSyllabus();
  refreshDiagnostics();
  startExamCountdown();
  loadLeaderboard();
  loadMistakeVault();
  loadTopicLessons();

  // Anti-cheat tab switch monitoring
  window.addEventListener("visibilitychange", handleAntiCheatEvent);
  window.addEventListener("blur", handleAntiCheatEvent);
});

// ----------------- ANTI-CHEAT ENGINE -----------------
function handleAntiCheatEvent() {
  const cbtView = document.getElementById("view-cbt");
  if (cbtView && cbtView.classList.contains("active") && filteredQuestions && filteredQuestions.length > 0) {
    if (document.hidden || !document.hasFocus()) {
      antiCheatSwitchCount++;
      const banner = document.getElementById("cbtAntiCheatBanner");
      const countDisplay = document.getElementById("cbtCheatCountDisplay");
      if (banner && countDisplay) {
        countDisplay.textContent = antiCheatSwitchCount;
        banner.style.display = "flex";
      }
    }
  }
}

function dismissAntiCheatWarning() {
  const banner = document.getElementById("cbtAntiCheatBanner");
  if (banner) banner.style.display = "none";
}

// ----------------- AUTHENTICATION & PROFILE -----------------
async function checkAuth() {
  try {
    const res = await fetch("/api/auth/me");
    const data = await res.json();
    if (data.status === "authenticated" && data.user) {
      currentUser = data.user;
      candidateName = currentUser.name;
      targetCourse = currentUser.target_course;
      targetUni = currentUser.target_uni;
      if (data.attempts) {
        sessionHistory = Object.assign({}, sessionHistory, data.attempts);
        Object.entries(data.attempts).forEach(([qId, att]) => {
          if (att.is_flagged) flaggedQuestions.add(qId);
        });
      }
      renderAuthHeader();
      refreshDiagnostics();
      renderPaletteGrid();
      loadMistakeVault();
      loadTopicLessons();
    } else {
      currentUser = null;
      renderAuthHeader();
    }
  } catch (err) {
    console.error("Auth check failed:", err);
  }
}

function renderAuthHeader() {
  const container = document.getElementById("authHeaderContainer");
  if (!container) return;

  if (currentUser) {
    const initial = currentUser.name.charAt(0).toUpperCase();
    const streak = currentUser.streak || 1;
    const planDisplay = (currentUser.plan && currentUser.plan !== 'free')
      ? `<span class="streak-badge" style="background: rgba(16, 185, 129, 0.2); color: #34d399; border-color: #10b981;" title="Active Subscription">👑 ${currentUser.plan.toUpperCase()} (${currentUser.days_left || 0}d left)</span>`
      : '';

    container.innerHTML = `
      <div style="display: flex; align-items: center; gap: 0.5rem;">
        ${planDisplay}
        <span class="streak-badge" title="Consecutive Practice Days">🔥 ${streak} Days</span>
        <span class="streak-badge" style="background: rgba(6, 182, 212, 0.15); color: var(--accent-cyan); border-color: rgba(6, 182, 212, 0.3);">
          ⭐ ${currentUser.xp || 120} XP
        </span>
        <div class="user-profile-badge" onclick="openProfileModal()" title="Candidate Profile & Account Settings">
          <div class="user-avatar-circle">${initial}</div>
          <span style="font-weight: 600;">${currentUser.name.split(" ")[0]}</span>
          <span style="font-size: 0.7rem; color: var(--text-dim);">⚙️</span>
        </div>
      </div>
    `;

    // Also update pricing active banner if present
    const subCard = document.getElementById("activeSubscriptionCard");
    if (subCard) {
      if (currentUser.plan && currentUser.plan !== 'free' && currentUser.days_left > 0) {
        subCard.style.display = "block";
        document.getElementById("activeCardTitle").textContent = "👑 Active Plan: " + currentUser.plan.toUpperCase() + " Master Pass";
        document.getElementById("activeCardDaysLeft").textContent = currentUser.days_left + " days, " + ((currentUser.hours_left || 0) % 24) + " hours";
      } else {
        subCard.style.display = "none";
      }
    }
  } else {
    container.innerHTML = `
      <button class="btn-pill" onclick="openAuthModal('login')">
        <span>🔐</span>
        <span>Login / Register</span>
      </button>
    `;
    const subCard = document.getElementById("activeSubscriptionCard");
    if (subCard) subCard.style.display = "none";
  }
}

function openAuthModal(mode = "login") {
  toggleAuthMode(mode);
  document.getElementById("authModal").classList.add("active");
}

function toggleAuthMode(mode) {
  const loginForm = document.getElementById("loginForm");
  const regForm = document.getElementById("registerForm");
  const tabLogin = document.getElementById("authTabLogin");
  const tabReg = document.getElementById("authTabRegister");

  if (mode === "login") {
    loginForm.style.display = "block";
    regForm.style.display = "none";
    tabLogin.classList.add("active");
    tabReg.classList.remove("active");
  } else {
    loginForm.style.display = "none";
    regForm.style.display = "block";
    tabLogin.classList.remove("active");
    tabReg.classList.add("active");
  }
}

async function handleLogin(e) {
  e.preventDefault();
  const id = document.getElementById("loginIdentifier").value.trim();
  const pwd = document.getElementById("loginPassword").value;

  try {
    const res = await fetch("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ identifier: id, password: pwd })
    });
    const data = await res.json();
    if (data.status === "success") {
      currentUser = data.user;
      candidateName = currentUser.name;
      targetCourse = currentUser.target_course;
      targetUni = currentUser.target_uni;
      if (data.attempts) {
        sessionHistory = Object.assign({}, sessionHistory, data.attempts);
      }
      renderAuthHeader();
      closeModal("authModal");
      refreshDiagnostics();
      loadLeaderboard();
      loadMistakeVault();
      loadTopicLessons();
      alert("👋 Welcome back, " + currentUser.name + "!");
    } else {
      alert("❌ " + data.error);
    }
  } catch (err) {
    alert("Login failed. Check your network connection.");
  }
}

async function handleRegister(e) {
  e.preventDefault();
  const name = document.getElementById("regName").value.trim();
  const email = document.getElementById("regEmail").value.trim();
  const phone = document.getElementById("regPhone").value.trim();
  const pwd = document.getElementById("regPassword").value;
  const uni = document.getElementById("regUni").value.trim();
  const course = document.getElementById("regCourse").value.trim();

  try {
    const res = await fetch("/api/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name, email, phone, password: pwd,
        target_uni: uni, target_course: course
      })
    });
    const data = await res.json();
    if (data.status === "success") {
      currentUser = data.user;
      candidateName = currentUser.name;
      targetCourse = currentUser.target_course;
      targetUni = currentUser.target_uni;
      renderAuthHeader();
      closeModal("authModal");
      refreshDiagnostics();
      loadLeaderboard();
      loadTopicLessons();
      alert("🎉 Account created successfully! Welcome to PassMaster AI, " + currentUser.name + ".");
    } else {
      alert("❌ " + data.error);
    }
  } catch (err) {
    alert("Registration failed. Check network.");
  }
}

async function handleLogout() {
  if (confirm("Log out of PassMaster AI?")) {
    await fetch("/api/auth/logout", { method: "POST" });
    currentUser = null;
    candidateName = "Candidate";
    closeModal("profileModal");
    renderAuthHeader();
    refreshDiagnostics();
  }
}


// ----------------- CANDIDATE STUDY PREFERENCES & IDENTITY PROTECTION -----------------
function getCandidatePreferences() {
  const saved = localStorage.getItem("passmaster_preferences");
  if (saved) {
    try {
      const parsed = JSON.parse(saved);
      return {
        questions_per_subject: parsed.questions_per_subject || 20,
        subjects: parsed.subjects || ["Use of English", "Mathematics", "Physics", "Chemistry"],
        target_course: parsed.target_course || "Medicine & Surgery",
        target_uni: parsed.target_uni || "UNILAG",
        target_score: parsed.target_score || 280,
        cbt_timer_mode: parsed.cbt_timer_mode || "standard",
        sound_enabled: parsed.sound_enabled !== undefined ? parsed.sound_enabled : true,
        socratic_hints: parsed.socratic_hints !== undefined ? parsed.socratic_hints : true
      };
    } catch (e) {}
  }
  return {
    questions_per_subject: 20,
    subjects: ["Use of English", "Mathematics", "Physics", "Chemistry"],
    target_course: (currentUser && currentUser.target_course) ? currentUser.target_course : "Medicine & Surgery",
    target_uni: (currentUser && currentUser.target_uni) ? currentUser.target_uni : "UNILAG",
    target_score: (currentUser && currentUser.target_score) ? currentUser.target_score : 280,
    cbt_timer_mode: "standard",
    sound_enabled: true,
    socratic_hints: true
  };
}

async function openPreferencesModal() {
  const modal = document.getElementById("profileModal");
  if (!modal) return;

  const prefs = getCandidatePreferences();

  // Populate locked identity credentials
  const initial = currentUser ? currentUser.name.charAt(0).toUpperCase() : "G";
  const avatarElem = document.getElementById("profileAvatarInitial");
  if (avatarElem) avatarElem.textContent = initial;

  const nameElem = document.getElementById("profileNameDisplay");
  if (nameElem) nameElem.textContent = currentUser ? currentUser.name : "Guest Candidate (Unregistered)";

  const emailElem = document.getElementById("profileEmailDisplay");
  if (emailElem) emailElem.textContent = currentUser ? currentUser.email : "guest@passmaster.ng (Locked)";

  const phoneElem = document.getElementById("profilePhoneDisplay");
  if (phoneElem) phoneElem.textContent = currentUser ? (currentUser.phone || "No phone recorded") : "0800-GUEST-000 (Locked)";

  const targetDisplay = document.getElementById("profileTargetDisplay");
  if (targetDisplay) targetDisplay.textContent = `${prefs.target_course} (${prefs.target_uni})`;

  const planDisplay = document.getElementById("profilePlanDisplay");
  if (planDisplay) planDisplay.textContent = ((currentUser && currentUser.plan) ? currentUser.plan : "Free").toUpperCase() + " TIER";

  const days = (currentUser && currentUser.days_left) || 0;
  const hours = ((currentUser && currentUser.hours_left) || 0) % 24;
  const daysText = (currentUser && currentUser.plan && currentUser.plan !== 'free' && days > 0)
    ? `👑 Active Pass: ${days} days, ${hours} hours remaining`
    : "Free Tier (Topic Masterclasses & Full Mocks Locked)";
  const daysBox = document.getElementById("profileDaysLeftText");
  if (daysBox) daysBox.textContent = daysText;

  // Set Question Per Subject selector
  const qPerSubj = prefs.questions_per_subject || 20;
  const hiddenQ = document.getElementById("prefQuestionsPerSubject");
  if (hiddenQ) hiddenQ.value = qPerSubj;

  const qLabel = document.getElementById("prefQCountLabel");
  if (qLabel) qLabel.textContent = `${qPerSubj} Qs per subject (${qPerSubj * 4} Total)`;

  document.querySelectorAll(".preference-pills-row .pref-pill-btn").forEach(btn => {
    btn.classList.toggle("active", btn.textContent.includes(`${qPerSubj} Qs`));
  });

  // Set Subject dropdowns
  const s2 = document.getElementById("prefSubj2");
  const s3 = document.getElementById("prefSubj3");
  const s4 = document.getElementById("prefSubj4");
  if (s2 && prefs.subjects[1]) s2.value = prefs.subjects[1];
  if (s3 && prefs.subjects[2]) s3.value = prefs.subjects[2];
  if (s4 && prefs.subjects[3]) s4.value = prefs.subjects[3];

  // Goals
  const courseInput = document.getElementById("prefTargetCourse");
  if (courseInput) courseInput.value = prefs.target_course;

  const uniInput = document.getElementById("prefTargetUni");
  if (uniInput) uniInput.value = prefs.target_uni;

  const scoreInput = document.getElementById("prefTargetScore");
  if (scoreInput) scoreInput.value = prefs.target_score;

  const timerSelect = document.getElementById("prefTimerMode");
  if (timerSelect) timerSelect.value = prefs.cbt_timer_mode;

  const soundCheck = document.getElementById("prefSoundCheck");
  if (soundCheck) soundCheck.checked = prefs.sound_enabled;

  const socraticCheck = document.getElementById("prefSocraticCheck");
  if (socraticCheck) socraticCheck.checked = prefs.socratic_hints;

  openModal("profileModal");
}

function openProfileModal() {
  openPreferencesModal();
}

function selectPrefQuestionsPerSubject(count, btnElem) {
  const hiddenQ = document.getElementById("prefQuestionsPerSubject");
  if (hiddenQ) hiddenQ.value = count;

  const qLabel = document.getElementById("prefQCountLabel");
  if (qLabel) qLabel.textContent = `${count} Qs per subject (${count * 4} Total)`;

  document.querySelectorAll(".preference-pills-row .pref-pill-btn").forEach(b => b.classList.remove("active"));
  if (btnElem) btnElem.classList.add("active");
}

function applySubjectPreset(preset) {
  const s2 = document.getElementById("prefSubj2");
  const s3 = document.getElementById("prefSubj3");
  const s4 = document.getElementById("prefSubj4");
  if (!s2 || !s3 || !s4) return;

  if (preset === 'medical') {
    s2.value = "Biology";
    s3.value = "Chemistry";
    s4.value = "Physics";
  } else if (preset === 'engineering') {
    s2.value = "Mathematics";
    s3.value = "Physics";
    s4.value = "Chemistry";
  } else if (preset === 'law') {
    s2.value = "Literature in English";
    s3.value = "Government";
    s4.value = "Economics";
  } else if (preset === 'commercial') {
    s2.value = "Mathematics";
    s3.value = "Economics";
    s4.value = "Government";
  }
}

async function saveCandidatePreferences() {
  const hiddenQ = document.getElementById("prefQuestionsPerSubject");
  const qPerSubj = hiddenQ ? parseInt(hiddenQ.value) || 20 : 20;

  const s2 = document.getElementById("prefSubj2") ? document.getElementById("prefSubj2").value : "Mathematics";
  const s3 = document.getElementById("prefSubj3") ? document.getElementById("prefSubj3").value : "Physics";
  const s4 = document.getElementById("prefSubj4") ? document.getElementById("prefSubj4").value : "Chemistry";

  const course = document.getElementById("prefTargetCourse") ? document.getElementById("prefTargetCourse").value.trim() : "Medicine & Surgery";
  const uni = document.getElementById("prefTargetUni") ? document.getElementById("prefTargetUni").value.trim() : "UNILAG";
  const score = document.getElementById("prefTargetScore") ? parseInt(document.getElementById("prefTargetScore").value) || 280 : 280;
  const timerMode = document.getElementById("prefTimerMode") ? document.getElementById("prefTimerMode").value : "standard";
  const soundEnabledVal = document.getElementById("prefSoundCheck") ? document.getElementById("prefSoundCheck").checked : true;
  const socraticVal = document.getElementById("prefSocraticCheck") ? document.getElementById("prefSocraticCheck").checked : true;

  const subjects = ["Use of English", s2, s3, s4];

  // Check unique subjects
  const uniqueSubs = new Set(subjects);
  if (uniqueSubs.size < 4) {
    alert("⚠️ Please choose 4 distinct subjects for your JAMB combination.");
    return;
  }

  const prefs = {
    questions_per_subject: qPerSubj,
    subjects: subjects,
    target_course: course,
    target_uni: uni,
    target_score: score,
    cbt_timer_mode: timerMode,
    sound_enabled: soundEnabledVal,
    socratic_hints: socraticVal
  };

  localStorage.setItem("passmaster_preferences", JSON.stringify(prefs));
  audioEnabled = soundEnabledVal;

  try {
    // Send to backend WITHOUT sensitive fields (name, email, phone, id)
    const res = await fetch("/api/auth/preferences", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(prefs)
    });
    const data = await res.json();
    if (data.status === "success") {
      alert(`✅ Study Preferences Saved Successfully!

• Questions per subject: ${qPerSubj} (Total: ${qPerSubj * 4} Qs)
• Active Subjects: ${subjects.join(", ")}
• Target: ${course} at ${uni} (${score}/400)
• Identity credentials remain verified and protected.`);
      
      closeModal("profileModal");
      
      // Reload CBT questions with new preferences
      await loadQuestions();
    } else {
      alert("❌ " + (data.error || "Failed to save preferences on server."));
    }
  } catch (err) {
    alert("Preferences saved locally. Server sync error: " + err);
  }
}


async function handleDeleteAccount() {
  if (!currentUser) return;
  const confirmed = confirm(
    `⚠️ ARE YOU ABSOLUTELY SURE?

This will permanently delete your account, practice history, and streaks.

IMPORTANT: If your email or phone is deleted more than 2 times, it will be automatically and permanently BANNED from registering again to prevent trial abuse.`
  );
  if (!confirmed) return;

  try {
    const res = await fetch("/api/auth/delete-account", {
      method: "POST",
      headers: { "Content-Type": "application/json" }
    });
    const data = await res.json();
    if (data.status === "deleted") {
      alert("✅ Your account has been permanently deleted.");
      currentUser = null;
      candidateName = "Candidate";
      sessionHistory = {};
      closeModal("profileModal");
      renderAuthHeader();
      refreshDiagnostics();
      switchView("dashboard");
    } else {
      alert("❌ " + (data.error || "Failed to delete account"));
    }
  } catch (err) {
    alert("Error deleting account: " + err);
  }
}

// ----------------- NAVIGATION -----------------
function switchView(viewName) {
  document.querySelectorAll(".view-section").forEach(sec => sec.classList.remove("active"));
  document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));

  const targetView = document.getElementById("view-" + viewName);
  const targetTab = document.getElementById("tab-" + viewName);

  if (targetView) targetView.classList.add("active");
  if (targetTab) targetTab.classList.add("active");

  if (viewName === "dashboard" || viewName === "leaks") {
    refreshDiagnostics();
  }
  if (viewName === "leaderboard") {
    loadLeaderboard();
  }
  if (viewName === "vault") {
    loadMistakeVault();
  }
  if (viewName === "lessons") {
    loadTopicLessons();
  }
}

// ----------------- QUESTIONS & CBT SIMULATOR -----------------
async function loadQuestions() {
  try {
    const prefs = getCandidatePreferences();
    const qPerSubj = prefs.questions_per_subject || 20;
    const subjects = prefs.subjects || ["Use of English", "Mathematics", "Physics", "Chemistry"];
    const url = `/api/questions?mode=jamb_standard&questions_per_subject=${qPerSubj}&subjects=${encodeURIComponent(subjects.join(','))}`;

    const res = await fetch(url);
    const data = await res.json();
    if (data.status === "success" && data.questions.length > 0) {
      allQuestions = data.questions;
      filteredQuestions = [...allQuestions];
      currentIndex = 0;
      renderCbtSubjectTabs();
      renderCbtTopicBar(currentActiveSubject);
      renderCurrentQuestion();
      renderPaletteGrid();
    }
  } catch (err) {
    console.error("Failed to load standard CBT questions:", err);
  }
}

function filterBySubject(subject, pillElem) {
  currentActiveSubject = subject;
  currentActiveTopic = "all";

  document.querySelectorAll(".subject-filter-bar .filter-pill").forEach(p => p.classList.remove("active"));
  if (pillElem) pillElem.classList.add("active");

  renderCbtTopicBar(subject);
  applyFilters();
}

function renderCbtTopicBar(subject) {
  const container = document.getElementById("cbtTopicPills");
  const countIndicator = document.getElementById("cbtTopicCountIndicator");
  const activeLabel = document.getElementById("activeTopicLabel");
  if (!container) return;

  container.innerHTML = "";

  const pool = (subject && subject !== "all")
    ? allQuestions.filter(q => q.subject.toLowerCase() === subject.toLowerCase())
    : allQuestions;

  const topicCounts = {};
  pool.forEach(q => {
    if (q.topic) {
      topicCounts[q.topic] = (topicCounts[q.topic] || 0) + 1;
    }
  });

  // Render "All Topics" pill
  const allPill = document.createElement("button");
  allPill.className = `topic-pill ${currentActiveTopic === "all" ? "active" : ""}`;
  allPill.innerHTML = `<span>🎯 All Topics</span> <span class="count-badge">${pool.length}</span>`;
  allPill.onclick = () => filterByTopic("all", allPill);
  container.appendChild(allPill);

  // Render pills for each topic in alphabetical order
  Object.keys(topicCounts).sort().forEach(topic => {
    const pill = document.createElement("button");
    const isActive = (currentActiveTopic.toLowerCase() === topic.toLowerCase());
    pill.className = `topic-pill ${isActive ? "active" : ""}`;
    pill.innerHTML = `<span>🔬 ${topic}</span> <span class="count-badge">${topicCounts[topic]}</span>`;
    pill.onclick = () => filterByTopic(topic, pill);
    container.appendChild(pill);
  });

  if (activeLabel) {
    activeLabel.textContent = currentActiveTopic === "all" ? "All Topics" : currentActiveTopic;
  }
  if (countIndicator) {
    const activeSubjDisplay = (subject && subject !== "all") ? subject : "All Subjects";
    countIndicator.textContent = `${pool.length} total in ${activeSubjDisplay}`;
  }
}

function filterByTopic(topicName, pillElem) {
  currentActiveTopic = topicName;

  const container = document.getElementById("cbtTopicPills");
  if (container) {
    container.querySelectorAll(".topic-pill").forEach(p => p.classList.remove("active"));
  }
  if (pillElem) pillElem.classList.add("active");

  const activeLabel = document.getElementById("activeTopicLabel");
  if (activeLabel) {
    activeLabel.textContent = topicName === "all" ? "All Topics" : topicName;
  }

  applyFilters();
}

function resetTopicFocus() {
  currentActiveTopic = "all";
  renderCbtTopicBar(currentActiveSubject);
  applyFilters();
}

function applyFilters() {
  let pool = allQuestions;

  if (currentActiveSubject && currentActiveSubject !== "all") {
    pool = pool.filter(q => q.subject.toLowerCase() === currentActiveSubject.toLowerCase());
  }

  if (currentActiveTopic && currentActiveTopic !== "all") {
    const norm = s => s.toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]/g, ' ').trim();
    const targetNorm = norm(currentActiveTopic);
    pool = pool.filter(q => {
      if (!q.topic) return false;
      if (q.topic.toLowerCase() === currentActiveTopic.toLowerCase()) return true;
      const qNorm = norm(q.topic);
      return qNorm.includes(targetNorm) || targetNorm.includes(qNorm);
    });
  }

  filteredQuestions = pool;
  currentIndex = 0;

  const countIndicator = document.getElementById("cbtTopicCountIndicator");
  if (countIndicator) {
    const topicDesc = currentActiveTopic === "all" ? "all topics" : currentActiveTopic;
    countIndicator.textContent = `${filteredQuestions.length} question${filteredQuestions.length === 1 ? '' : 's'} available (${topicDesc})`;
  }

  renderCurrentQuestion();
  renderPaletteGrid();
}

function renderCurrentQuestion() {
  if (!filteredQuestions || filteredQuestions.length === 0) return;

  const q = filteredQuestions[currentIndex];
  document.getElementById("cbtSubjectBadge").textContent = q.subject;
  document.getElementById("cbtYearBadge").textContent = "JAMB " + q.year;
  document.getElementById("cbtTopicBadge").textContent = "Topic: " + q.topic + " (" + q.subtopic + ")";
  document.getElementById("cbtQuestionText").textContent = q.question;
  const currentSubj = q.subject;
  const subjPool = filteredQuestions.filter(x => x.subject === currentSubj);
  const subjIdx = subjPool.findIndex(x => x.id === q.id) + 1;
  document.getElementById("qCounterDisplay").textContent = `Question ${currentIndex + 1} of ${filteredQuestions.length} (${currentSubj}: ${subjIdx}/${subjPool.length})`;
  renderCbtSubjectTabs();

  const flagBtn = document.getElementById("flagQuestionBtn");
  if (flagBtn) {
    flagBtn.style.color = flaggedQuestions.has(q.id) ? "var(--accent-amber)" : "var(--text-main)";
    flagBtn.style.borderColor = flaggedQuestions.has(q.id) ? "var(--accent-amber)" : "var(--border-subtle)";
  }

  const optsContainer = document.getElementById("cbtOptionsList");
  optsContainer.innerHTML = "";

  const savedAttempt = sessionHistory[q.id];

  Object.entries(q.options).forEach(([key, val]) => {
    const btn = document.createElement("button");
    btn.className = "option-btn";
    btn.dataset.option = key;

    if (savedAttempt) {
      if (savedAttempt.selected === key) {
        btn.classList.add(savedAttempt.is_correct ? "correct" : "wrong");
      } else if (savedAttempt.is_correct && key === q.correct_option) {
        btn.classList.add("correct");
      }
    }

    btn.innerHTML = `<div class="option-badge">${key}</div><div style="flex: 1;">${val}</div>`;
    btn.onclick = () => selectOption(q.id, key);
    optsContainer.appendChild(btn);
  });

  resetTimer();
  renderPaletteGrid();
}

function renderPaletteGrid() {
  const grid = document.getElementById("questionPaletteGrid");
  if (!grid || !filteredQuestions) return;
  grid.innerHTML = "";

  filteredQuestions.forEach((q, idx) => {
    const btn = document.createElement("button");
    btn.className = "palette-btn";
    btn.textContent = idx + 1;

    if (idx === currentIndex) {
      btn.classList.add("current");
    }

    if (sessionHistory[q.id]) {
      btn.classList.add("answered");
    }

    if (flaggedQuestions.has(q.id)) {
      btn.classList.add("flagged");
    }

    btn.onclick = () => {
      currentIndex = idx;
      renderCurrentQuestion();
    };

    grid.appendChild(btn);
  });
}

function toggleFlagCurrentQuestion() {
  const q = filteredQuestions[currentIndex];
  if (!q) return;
  if (flaggedQuestions.has(q.id)) {
    flaggedQuestions.delete(q.id);
  } else {
    flaggedQuestions.add(q.id);
  }
  renderCurrentQuestion();
}

async function selectOption(questionId, selectedKey) {
  try {
    const timeSpent = 40 - timerSeconds;
    const isFlagged = flaggedQuestions.has(questionId);

    const res = await fetch("/api/tutor/attempt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question_id: questionId,
        selected_option: selectedKey,
        time_seconds: Math.max(5, timeSpent),
        is_flagged: isFlagged
      })
    });

    const result = await res.json();

    sessionHistory[questionId] = {
      selected: selectedKey,
      is_correct: result.is_correct,
      time_seconds: Math.max(5, timeSpent),
      is_flagged: isFlagged
    };

    // Play Sound FX
    playSound(result.is_correct ? "correct" : "wrong");

    document.querySelectorAll(".option-btn").forEach(btn => {
      btn.classList.remove("selected", "correct", "wrong");
      if (btn.dataset.option === selectedKey) {
        btn.classList.add(result.is_correct ? "correct" : "wrong");
      }
    });

    appendCoachMessage(result.message);
    if (audioEnabled) {
      speakCoachText(result.message);
    }
    refreshDiagnostics();
    renderPaletteGrid();
    renderCbtSubjectTabs();
    loadMistakeVault();
  } catch (err) {
    console.error("Error submitting attempt:", err);
  }
}

function nextQuestion() {
  if (currentIndex < filteredQuestions.length - 1) {
    currentIndex++;
    renderCurrentQuestion();
  }
}

function prevQuestion() {
  if (currentIndex > 0) {
    currentIndex--;
    renderCurrentQuestion();
  }
}

function resetTimer() {
  if (cbtMode === 'full_jamb') {
    // In full JAMB mode, the global mock timer is ticking
    return;
  }
  clearInterval(timerInterval);
  timerSeconds = 40;
  updateTimerDisplay();

  timerInterval = setInterval(() => {
    timerSeconds--;
    updateTimerDisplay();
    if (timerSeconds <= 0) {
      clearInterval(timerInterval);
    }
  }, 1000);
}

function updateTimerDisplay() {
  const min = Math.floor(timerSeconds / 60);
  const sec = timerSeconds % 60;
  const timerElem = document.getElementById("timerDisplay");
  if (timerElem) {
    timerElem.textContent = String(min).padStart(2, "0") + ":" + String(sec).padStart(2, "0");
  }
}

// ----------------- CBT SETUP MODAL & MODES -----------------
let currentSetupMode = 'drill';

function openCbtSetupModal() {
  currentSetupMode = 'drill';
  setCbtSetupMode('drill');
  onSetupSubjectChanged();
  openModal('cbtSetupModal');
}

function setCbtSetupMode(mode) {
  currentSetupMode = mode;
  const btnDrill = document.getElementById("modeBtnDrill");
  const btnMock = document.getElementById("modeBtnMock");
  const subjGroup = document.getElementById("cbtSubjectGroup");
  const topicGroup = document.getElementById("cbtTopicGroup");
  const limitGroup = document.getElementById("cbtLimitGroup");
  const randomGroup = document.getElementById("cbtRandomGroup");
  const noticeBox = document.getElementById("fullJambNoticeBox");

  if (mode === 'full_jamb') {
    if (btnDrill) btnDrill.classList.remove("active");
    if (btnMock) btnMock.classList.add("active");
    if (subjGroup) subjGroup.style.display = "none";
    if (topicGroup) topicGroup.style.display = "none";
    if (limitGroup) limitGroup.style.display = "none";
    if (randomGroup) randomGroup.style.display = "none";
    if (noticeBox) noticeBox.style.display = "block";
  } else {
    if (btnDrill) btnDrill.classList.add("active");
    if (btnMock) btnMock.classList.remove("active");
    if (subjGroup) subjGroup.style.display = "block";
    if (topicGroup) topicGroup.style.display = "block";
    if (limitGroup) limitGroup.style.display = "block";
    if (randomGroup) randomGroup.style.display = "flex";
    if (noticeBox) noticeBox.style.display = "none";
  }
}

function onSetupSubjectChanged() {
  const subjSelect = document.getElementById("setupSubjectSelect");
  const topicSelect = document.getElementById("setupTopicSelect");
  if (!topicSelect) return;
  topicSelect.innerHTML = '<option value="">-- All Topics in Subject --</option>';

  const subj = subjSelect ? subjSelect.value : "all";
  if (subj !== 'all') {
    // Populate topics directly from loaded question bank
    const topicMap = {};
    if (allQuestions && allQuestions.length > 0) {
      allQuestions
        .filter(q => q.subject.toLowerCase() === subj.toLowerCase())
        .forEach(q => {
          if (q.topic) {
            topicMap[q.topic] = (topicMap[q.topic] || 0) + 1;
          }
        });
    }

    if (Object.keys(topicMap).length > 0) {
      Object.keys(topicMap).sort().forEach(topName => {
        const opt = document.createElement("option");
        opt.value = topName;
        opt.textContent = `${topName} (${topicMap[topName]} questions)`;
        topicSelect.appendChild(opt);
      });
    } else if (syllabusData && syllabusData[subj]) {
      syllabusData[subj].topics.forEach(t => {
        const opt = document.createElement("option");
        opt.value = t.name;
        opt.textContent = `${t.name} (${t.weight_pct}% weight)`;
        topicSelect.appendChild(opt);
      });
    }
  }
}

async function startCustomCbtSession() {
  closeModal('cbtSetupModal');
  antiCheatSwitchCount = 0;
  const banner = document.getElementById("cbtAntiCheatBanner");
  if (banner) banner.style.display = "none";

  if (currentSetupMode === 'full_jamb') {
    cbtMode = 'full_jamb';
    examTimeRemaining = 7200; // 120 minutes = 2 hours
    try {
      const res = await fetch('/api/questions?mode=full_jamb');
      const data = await res.json();
      if (data.status === 'success' && data.questions.length > 0) {
        filteredQuestions = data.questions;
        currentIndex = 0;
        switchView('cbt');
        renderCurrentQuestion();
        renderPaletteGrid();
        startFullJambTimer();
        alert(`🏆 Full 120-Minute JAMB CBT Simulation Launched!

180 Questions across 4 subjects loaded.
Official 2-Hour countdown started.
Anti-cheat monitoring is active!`);
      } else {
        alert('Failed to load Full JAMB exam questions.');
      }
    } catch (err) {
      alert('Error launching Full JAMB mock: ' + err);
    }
  } else {
    cbtMode = 'drill';
    clearInterval(fullJambTimerInterval);
    const subj = document.getElementById("setupSubjectSelect").value;
    const topic = document.getElementById("setupTopicSelect").value;
    const limit = document.getElementById("setupLimitSelect").value;
    const random = document.getElementById("setupRandomCheck").checked;

    let url = `/api/questions?limit=${limit}&random=${random}`;
    if (subj && subj !== 'all') url += `&subject=${encodeURIComponent(subj)}`;
    if (topic) url += `&topic=${encodeURIComponent(topic)}`;

    try {
      const res = await fetch(url);
      const data = await res.json();
      if (data.status === 'success' && data.questions.length > 0) {
        currentActiveSubject = (subj && subj !== 'all') ? subj : 'all';
        currentActiveTopic = topic ? topic : 'all';

        // Update subject filter pills
        document.querySelectorAll(".subject-filter-bar .filter-pill").forEach(p => {
          p.classList.toggle("active", p.textContent.toLowerCase().includes(currentActiveSubject.toLowerCase()) || (currentActiveSubject === 'all' && p.textContent.includes('All')));
        });

        renderCbtTopicBar(currentActiveSubject);
        filteredQuestions = data.questions;
        currentIndex = 0;
        switchView('cbt');
        renderCurrentQuestion();
        renderPaletteGrid();
      } else {
        alert('No questions found matching your filter.');
      }
    } catch (err) {
      alert('Error loading drill questions: ' + err);
    }
  }
}

function startFullJambTimer() {
  clearInterval(timerInterval);
  clearInterval(fullJambTimerInterval);
  updateFullJambTimerDisplay();

  fullJambTimerInterval = setInterval(() => {
    examTimeRemaining--;
    updateFullJambTimerDisplay();

    if (examTimeRemaining <= 0) {
      clearInterval(fullJambTimerInterval);
      alert('⏰ TIME IS UP! Your 120-minute JAMB CBT Mock has ended. Generating official scorecard...');
      openShareModal();
    }
  }, 1000);
}

function updateFullJambTimerDisplay() {
  const hours = Math.floor(examTimeRemaining / 3600);
  const min = Math.floor((examTimeRemaining % 3600) / 60);
  const sec = examTimeRemaining % 60;
  const timerElem = document.getElementById("timerDisplay");
  if (timerElem) {
    timerElem.textContent = `${String(hours).padStart(2, "0")}:${String(min).padStart(2, "0")}:${String(sec).padStart(2, "0")}`;
  }
}

// ----------------- TOPIC MASTERCLASS LESSONS -----------------
async function loadTopicLessons() {
  try {
    const res = await fetch("/api/lessons");
    const data = await res.json();
    if (data.status === "success") {
      loadedLessons = data.lessons;
      renderLessonCards(loadedLessons);
    }
  } catch (err) {
    console.error("Failed to load lessons:", err);
  }
}

function renderLessonCards(lessons) {
  const container = document.getElementById("lessonsCardsContainer");
  if (!container) return;
  container.innerHTML = "";

  lessons.forEach((les) => {
    const card = document.createElement("div");
    card.className = "card";
    card.style.display = "flex";
    card.style.flexDirection = "column";
    card.style.justifyContent = "space-between";
    card.style.border = les.is_locked ? "1px solid rgba(148, 163, 184, 0.2)" : "1px solid rgba(56, 189, 248, 0.4)";
    card.style.background = les.is_locked ? "rgba(15, 23, 42, 0.6)" : "var(--bg-card)";

    const lockBadge = les.is_locked
      ? `<span class="status-badge" style="background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3);">🔒 Paid Pass</span>`
      : `<span class="status-badge status-confirmed">✨ Free Preview</span>`;

    card.innerHTML = `
      <div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
          <span class="subject-badge">${les.subject}</span>
          ${lockBadge}
        </div>
        <h4 style="font-size: 1.05rem; font-weight: 700; color: #ffffff; margin-bottom: 0.35rem;">${les.title}</h4>
        <div style="font-size: 0.78rem; color: var(--accent-cyan); font-weight: 600; margin-bottom: 0.5rem;">Topic: ${les.topic}</div>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 1rem;">${les.summary}</p>
      </div>
      <div>
        <button class="btn-pill ${les.is_locked ? '' : 'btn-primary'}" style="width: 100%; justify-content: center;" onclick="viewLesson('${les.subject.replace(/'/g, "\'")}', '${les.topic.replace(/'/g, "\'")}', ${les.is_locked})">
          ${les.is_locked ? '🔒 Unlock Masterclass' : '📖 Read Masterclass'}
        </button>
      </div>
    `;
    container.appendChild(card);
  });
}

function filterLessonsBySubject(subject, pillElem) {
  document.querySelectorAll("#lessonsFilterBar .filter-pill").forEach(p => p.classList.remove("active"));
  if (pillElem) pillElem.classList.add("active");

  if (subject === "all") {
    renderLessonCards(loadedLessons);
  } else {
    const filtered = loadedLessons.filter(l => l.subject.toLowerCase() === subject.toLowerCase());
    renderLessonCards(filtered);
  }
}

async function viewLesson(subject, topic, isLocked) {
  if (isLocked) {
    if (confirm(`🔒 This Topic Masterclass is exclusive to PassMaster subscribers.

Would you like to unlock all 32 lessons and full mocks now?`)) {
      openPaymentModal('weekly');
    }
    return;
  }

  try {
    const res = await fetch(`/api/lessons/${encodeURIComponent(subject)}/${encodeURIComponent(topic)}`);
    const data = await res.json();
    if (data.status === "success") {
      const les = data.lesson;
      activeLessonData = les;

      // Badges
      const subjBadge = document.getElementById("lessonSubjectBadge");
      if (subjBadge) subjBadge.textContent = les.subject;

      const topBadge = document.getElementById("lessonTopicBadge");
      if (topBadge) topBadge.textContent = les.topic;

      const catBadge = document.getElementById("lessonCategoryBadge");
      if (catBadge) catBadge.textContent = les.category || "Core Syllabus Masterclass";

      const wtBadge = document.getElementById("lessonWeightBadge");
      if (wtBadge) wtBadge.textContent = les.jamb_weight || "High Weight";

      const titleElem = document.getElementById("lessonModalTitle");
      if (titleElem) titleElem.textContent = les.title;

      // Learn from scratch primer
      const scratchContainer = document.getElementById("lessonFromScratchContainer");
      const scratchText = document.getElementById("lessonFromScratchText");
      if (les.from_scratch_guide && scratchText && scratchContainer) {
        scratchText.textContent = les.from_scratch_guide;
        scratchContainer.style.display = "block";
      } else if (scratchContainer) {
        scratchContainer.style.display = "none";
      }

      // Key rule / formula
      const ruleElem = document.getElementById("lessonKeyRule");
      if (ruleElem) ruleElem.textContent = les.key_rule_or_formula || "Master core syllabus principles.";

      // Deep dive content
      const contentElem = document.getElementById("lessonContentText");
      if (contentElem) contentElem.textContent = les.content;

      // Traps & Tip
      const trapsElem = document.getElementById("lessonTrapsText");
      if (trapsElem) trapsElem.textContent = les.common_traps || "Watch out for subtle distractors and misleading units.";

      const tipElem = document.getElementById("lessonTipText");
      if (tipElem) tipElem.textContent = les.secret_tip || "Eliminate extremes and calculate order of magnitude first.";

      // Worked Examples
      renderWorkedExamples(les.worked_examples || []);

      // Visual Diagrams & Video Theater
      renderTopicVisual(les.subject, les.topic);
      renderTopicVideo(les.video_meta, les.title);

      // Prerequisites & Next steps
      renderPrerequisites(les.prerequisites || [], les.prepares_for || [], les.subject);

      // Reset to text tab
      switchLessonModalTab('text');

      openModal("lessonModal");
    } else {
      if (res.status === 403) {
        alert("🔒 " + data.error);
        openPaymentModal('weekly');
      } else {
        alert("Error loading lesson: " + (data.error || "Unknown error"));
      }
    }
  } catch (err) {
    alert("Failed to load lesson details: " + err);
  }
}

async function practiceCurrentTopicQuestions() {
  if (!activeLessonData) return;
  const subj = activeLessonData.subject;
  const topic = activeLessonData.topic;
  closeModal("lessonModal");

  try {
    const res = await fetch(`/api/questions?subject=${encodeURIComponent(subj)}&topic=${encodeURIComponent(topic)}&limit=5&random=true`);
    const data = await res.json();
    if (data.status === "success" && data.questions.length > 0) {
      filteredQuestions = data.questions;
      currentIndex = 0;
      switchView("cbt");
      renderCurrentQuestion();
      renderPaletteGrid();
      alert(`🎯 Ready! Loaded 5 practice questions for:
${subj} — ${topic}`);
    } else {
      // Fall back to subject questions
      const fbRes = await fetch(`/api/questions?subject=${encodeURIComponent(subj)}&limit=5&random=true`);
      const fbData = await fbRes.json();
      if (fbData.status === "success" && fbData.questions.length > 0) {
        filteredQuestions = fbData.questions;
        currentIndex = 0;
        switchView("cbt");
        renderCurrentQuestion();
        renderPaletteGrid();
      }
    }
  } catch (err) {
    alert("Error loading topic questions: " + err);
  }
}

// ----------------- SOCRATIC COACH CHAT & AUDIO -----------------
async function handleCoachChatSubmit(e) {
  e.preventDefault();
  const input = document.getElementById("coachMessageInput");
  const msg = input.value.trim();
  if (!msg) return;

  const currentQ = (filteredQuestions && filteredQuestions[currentIndex]) ? filteredQuestions[currentIndex] : null;
  const qId = currentQ ? currentQ.id : null;
  appendStudentMessage(msg);
  input.value = "";

  try {
    const res = await fetch("/api/tutor/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question_id: qId, message: msg })
    });
    const data = await res.json();
    appendCoachMessage(data.reply);
    if (audioEnabled) {
      speakCoachText(data.reply);
    }
  } catch (err) {
    console.error("Error with coach chat:", err);
    appendCoachMessage("⚠️ Network hiccup. Coach Kalu is reconnecting...");
  }
}

function appendCoachMessage(text) {
  const chatArea = document.getElementById("coachChatArea");
  if (!chatArea) return;
  const bubble = document.createElement("div");
  bubble.className = "chat-bubble coach";
  bubble.textContent = text;
  chatArea.appendChild(bubble);
  chatArea.scrollTop = chatArea.scrollHeight;
}

function appendStudentMessage(text) {
  const chatArea = document.getElementById("coachChatArea");
  if (!chatArea) return;
  const bubble = document.createElement("div");
  bubble.className = "chat-bubble student";
  bubble.textContent = text;
  chatArea.appendChild(bubble);
  chatArea.scrollTop = chatArea.scrollHeight;
}

function toggleAudioCoach() {
  audioEnabled = !audioEnabled;
  const btn = document.getElementById("audioToggleBtn");
  if (btn) {
    btn.innerHTML = audioEnabled ? "<span>🔊</span> Audio On" : "<span>🔇</span> Audio Muted";
  }
  if (!audioEnabled && window.speechSynthesis) {
    window.speechSynthesis.cancel();
  }
}

function speakCoachText(text) {
  if (!window.speechSynthesis || !audioEnabled) return;
  window.speechSynthesis.cancel();
  const clean = text.replace(/[*_#🎯⚠️💡👉📌🔥⚡]/g, "").split(String.fromCharCode(10)).join(". ");
  const utter = new SpeechSynthesisUtterance(clean);
  utter.rate = 1.0;
  utter.pitch = 1.0;
  window.speechSynthesis.speak(utter);
}

// ----------------- MISTAKE VAULT -----------------
async function loadMistakeVault() {
  try {
    const res = await fetch("/api/mistake-vault");
    const data = await res.json();
    const container = document.getElementById("mistakeVaultContainer");
    if (!container) return;

    if (!data.vault || data.vault.length === 0) {
      container.innerHTML = `
        <div style="text-align: center; padding: 2rem; color: var(--text-muted);">
          🎉 <strong>Clean Sheet!</strong> You haven't made any mistakes yet. Practice questions in CBT mode to log cognitive errors here.
        </div>
      `;
      return;
    }

    container.innerHTML = "";
    data.vault.forEach(m => {
      const card = document.createElement("div");
      card.className = "vault-card";
      card.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
          <span class="subject-badge">${m.subject}</span>
          <span style="font-size: 0.75rem; color: var(--text-dim);">${m.topic} (${m.subtopic})</span>
        </div>
        <h4>${m.question}</h4>
        <div style="font-size: 0.82rem; color: var(--accent-rose); margin-bottom: 0.4rem;">
          ❌ <strong>Your Choice:</strong> Option ${m.your_wrong_choice} (Incorrect)
        </div>
        <div style="font-size: 0.82rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">
          ✅ <strong>Correct Option:</strong> Option ${m.correct_option}
        </div>
        <div style="background: rgba(239, 68, 68, 0.1); border-left: 3px solid var(--accent-rose); padding: 0.5rem 0.75rem; border-radius: 4px; font-size: 0.8rem; color: #fca5a5; margin-bottom: 0.5rem;">
          <strong>Why you fell into this trap:</strong> ${m.why_it_is_wrong}
        </div>
        <div style="font-size: 0.8rem; color: var(--accent-cyan);">
          💡 <strong>Correct Rule:</strong> ${m.explanation}
        </div>
      `;
      container.appendChild(card);
    });
  } catch (err) {
    console.error("Error loading mistake vault:", err);
  }
}

// ----------------- LEADERBOARD -----------------
async function loadLeaderboard() {
  try {
    const res = await fetch("/api/leaderboard");
    const data = await res.json();
    const tbody = document.getElementById("leaderboardTbody");
    if (!tbody || !data.leaderboard) return;

    tbody.innerHTML = "";
    data.leaderboard.forEach(r => {
      const tr = document.createElement("tr");
      let rankBadge = `<span class="rank-badge">${r.rank}</span>`;
      if (r.rank === 1) rankBadge = `<span class="rank-badge rank-1">🥇</span>`;
      else if (r.rank === 2) rankBadge = `<span class="rank-badge rank-2">🥈</span>`;
      else if (r.rank === 3) rankBadge = `<span class="rank-badge rank-3">🥉</span>`;

      tr.innerHTML = `
        <td>${rankBadge}</td>
        <td><strong>${r.name}</strong></td>
        <td><span style="color: var(--text-muted); font-size: 0.8rem;">${r.target_course} at ${r.target_uni}</span></td>
        <td><strong style="color: var(--accent-cyan); font-family: monospace;">${r.xp} XP</strong></td>
        <td><span style="color: var(--accent-emerald); font-weight: 700;">${r.predicted_score} / 400</span></td>
      `;
      tbody.appendChild(tr);
    });
  } catch (err) {
    console.error("Error loading leaderboard:", err);
  }
}

// ----------------- ON-SCREEN CALCULATOR -----------------
function calcNum(val) {
  if (calcCurrent === "0" && val !== ".") {
    calcCurrent = val;
  } else {
    calcCurrent += val;
  }
  updateCalcScreen();
}

function calcAction(act) {
  if (act === "C") {
    calcCurrent = "0";
    calcPrev = null;
    calcOp = null;
  } else if (act === "CE") {
    calcCurrent = "0";
  } else if (act === "sqrt") {
    const n = parseFloat(calcCurrent);
    calcCurrent = String(Math.sqrt(n));
  } else if (act === "pi") {
    calcCurrent = String(Math.PI);
  } else if (["+", "-", "*", "/"].includes(act)) {
    calcPrev = parseFloat(calcCurrent);
    calcOp = act;
    calcCurrent = "0";
  } else if (act === "=") {
    if (calcPrev !== null && calcOp) {
      const b = parseFloat(calcCurrent);
      let res = 0;
      if (calcOp === "+") res = calcPrev + b;
      else if (calcOp === "-") res = calcPrev - b;
      else if (calcOp === "*") res = calcPrev * b;
      else if (calcOp === "/") res = b !== 0 ? calcPrev / b : "Error";
      calcCurrent = String(res);
      calcPrev = null;
      calcOp = null;
    }
  }
  updateCalcScreen();
}

function updateCalcScreen() {
  const scr = document.getElementById("calcScreen");
  if (scr) scr.textContent = calcCurrent;
}

// ----------------- DIAGNOSTICS & SCORE PREDICTOR -----------------
async function refreshDiagnostics() {
  try {
    const res = await fetch("/api/diagnostics/score", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ history: sessionHistory })
    });

    const data = await res.json();
    if (data.status === "success") {
      const pred = data.predicted_score;
      const score = pred.total_predicted_score;

      const scoreElem = document.getElementById("predictedScoreDisplay");
      if (scoreElem) scoreElem.textContent = score;

      const badge = document.getElementById("readinessBadge");
      if (badge) {
        badge.textContent = pred.readiness_level;
        badge.style.color = pred.readiness_color;
        badge.style.borderColor = pred.readiness_color;
      }

      const dial = document.getElementById("scoreDial");
      if (dial) {
        const pct = Math.round((score / 400) * 100);
        dial.style.setProperty("--score-pct", pct);
      }

      renderLeaks(data.leaky_bucket);
    }
  } catch (err) {
    console.error("Error refreshing diagnostics:", err);
  }
}

function renderLeaks(leaks) {
  const dashContainer = document.getElementById("dashboardLeaksContainer");
  const allContainer = document.getElementById("allLeaksContainer");

  if (!dashContainer || !allContainer) return;

  dashContainer.innerHTML = "";
  allContainer.innerHTML = "";

  if (!leaks || leaks.length === 0) {
    const emptyMsg = `<div style="padding: 1rem; text-align: center; color: var(--text-muted); font-size: 0.85rem;">
      🎯 No mark leaks recorded yet! Complete at least 2 questions in CBT mode to diagnose your weak spots.
    </div>`;
    dashContainer.innerHTML = emptyMsg;
    allContainer.innerHTML = emptyMsg;
    return;
  }

  leaks.slice(0, 2).forEach(leak => {
    dashContainer.appendChild(createLeakCard(leak));
  });

  leaks.forEach(leak => {
    allContainer.appendChild(createLeakCard(leak, true));
  });
}

function createLeakCard(leak, showConcept = false) {
  const div = document.createElement("div");
  div.className = "leak-item";
  div.innerHTML = `
    <div class="leak-info">
      <h4>${leak.subject}: ${leak.subtopic}</h4>
      <p>Topic: ${leak.topic}</p>
      ${showConcept ? `<p style="color: var(--accent-cyan); font-size: 0.75rem; margin-top: 0.3rem;">💡 Rule: ${leak.pedagogical_concept}</p>` : ""}
    </div>
    <div class="leak-stat">
      <div class="mark-loss">-${leak.estimated_mark_loss} marks</div>
      <div class="accuracy">${leak.accuracy_pct}% accuracy</div>
    </div>
  `;
  return div;
}

// ----------------- SYLLABUS RENDER -----------------
async function loadSyllabus() {
  try {
    const res = await fetch("/api/syllabus");
    const data = await res.json();
    if (data.status === "success") {
      syllabusData = data.syllabus;
      renderSyllabus(data.syllabus);
    }
  } catch (err) {
    console.error("Failed to load syllabus:", err);
  }
}

function renderSyllabus(syllabus) {
  const container = document.getElementById("syllabusGrid");
  if (!container) return;
  container.innerHTML = "";

  Object.entries(syllabus).forEach(([subject, details]) => {
    const card = document.createElement("div");
    card.style.background = "var(--bg-card)";
    card.style.padding = "0.85rem";
    card.style.borderRadius = "var(--radius-sm)";
    card.style.border = "1px solid var(--border-subtle)";

    const topicsHtml = details.topics.map(t => `
      <div style="display: flex; justify-content: space-between; font-size: 0.78rem; color: var(--text-muted); margin-top: 0.25rem;">
        <span>${t.name}</span>
        <span style="color: var(--accent-cyan); font-weight: 600;">${t.weight_pct}% weight</span>
      </div>
    `).join("");

    card.innerHTML = `
      <h4 style="font-size: 0.95rem; font-weight: 700; color: #ffffff; margin-bottom: 0.4rem;">${subject}</h4>
      <div style="font-size: 0.72rem; color: var(--text-dim); text-transform: uppercase; margin-bottom: 0.4rem;">${details.weight_in_jamb} Questions in JAMB</div>
      ${topicsHtml}
    `;
    container.appendChild(card);
  });
}

// ----------------- PARENT PORTAL -----------------
async function lookupParentReport() {
  const phone = document.getElementById("parentPhoneInput").value.trim();
  const container = document.getElementById("parentReportResult");
  if (!phone) {
    alert("Please enter a phone number");
    return;
  }

  try {
    const res = await fetch(`/api/parent/report?phone=${encodeURIComponent(phone)}`);
    const data = await res.json();
    if (data.status === "success") {
      const r = data.report;
      container.innerHTML = `
        <div class="card" style="border: 1px solid var(--accent-cyan);">
          <div class="card-title-row">
            <h3 style="font-size: 1.15rem; font-weight: 800; color: #ffffff;">👤 ${r.name}</h3>
            <span class="streak-badge">🔥 ${r.streak_days} Days Streak</span>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 0.75rem; margin: 1rem 0;">
            <div style="background: var(--bg-card); padding: 0.75rem; border-radius: 8px; text-align: center;">
              <div style="font-size: 0.75rem; color: var(--text-dim);">Target University</div>
              <strong style="color: #ffffff; font-size: 0.95rem;">${r.target_uni}</strong>
            </div>
            <div style="background: var(--bg-card); padding: 0.75rem; border-radius: 8px; text-align: center;">
              <div style="font-size: 0.75rem; color: var(--text-dim);">Target Course</div>
              <strong style="color: #ffffff; font-size: 0.95rem;">${r.target_course}</strong>
            </div>
            <div style="background: var(--bg-card); padding: 0.75rem; border-radius: 8px; text-align: center;">
              <div style="font-size: 0.75rem; color: var(--text-dim);">Practice Accuracy</div>
              <strong style="color: var(--accent-emerald); font-size: 1.1rem;">${r.accuracy_pct}%</strong>
            </div>
            <div style="background: var(--bg-card); padding: 0.75rem; border-radius: 8px; text-align: center;">
              <div style="font-size: 0.75rem; color: var(--text-dim);">Questions Answered</div>
              <strong style="color: var(--accent-cyan); font-size: 1.1rem;">${r.questions_completed}</strong>
            </div>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(6, 182, 212, 0.1); padding: 0.75rem 1rem; border-radius: 8px;">
            <div>
              <span style="font-size: 0.8rem; color: var(--text-muted);">Current Subscription Plan:</span>
              <strong style="text-transform: uppercase; color: var(--accent-cyan); margin-left: 0.4rem;">${r.plan}</strong>
            </div>
            <span style="font-size: 0.8rem; font-weight: 700; color: ${r.is_active ? "var(--accent-emerald)" : "var(--accent-amber)"};">
              ${r.is_active ? "● Active Pass" : "⚠️ Needs Pass Renewal"}
            </span>
          </div>
        </div>
      `;
    } else {
      container.innerHTML = `<div style="text-align: center; padding: 1.5rem; color: var(--accent-rose);">❌ ${data.error || "No student found with this phone number."}</div>`;
    }
  } catch (err) {
    container.innerHTML = `<div style="text-align: center; padding: 1.5rem; color: var(--accent-rose);">Error connecting to student registry.</div>`;
  }
}

// ----------------- WHATSAPP BOT SIMULATOR -----------------
async function handleWhatsAppSend(e) {
  e.preventDefault();
  const input = document.getElementById("waUserInput");
  const msg = input.value.trim();
  if (!msg) return;

  const canvas = document.getElementById("waChatCanvas");
  
  const userBubble = document.createElement("div");
  userBubble.className = "wa-msg user";
  userBubble.textContent = msg;
  canvas.appendChild(userBubble);
  input.value = "";
  canvas.scrollTop = canvas.scrollHeight;

  try {
    const res = await fetch("/api/whatsapp/message", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ phone: currentUser ? currentUser.phone : "2348091977795", message: msg })
    });
    const data = await res.json();
    
    const botBubble = document.createElement("div");
    botBubble.className = "wa-msg bot";
    botBubble.textContent = data.reply;
    canvas.appendChild(botBubble);
    canvas.scrollTop = canvas.scrollHeight;
  } catch (err) {
    console.error("WhatsApp error:", err);
  }
}

// ----------------- MODALS & PAYMENTS -----------------
function openModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.add("active");
}

function closeModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.remove("active");
}

let currentCheckoutRef = null;

async function openPaymentModal(planId) {
  activePlan = planId;
  const modal = document.getElementById("paymentModal");
  const res = await fetch("/api/payments/checkout", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ plan_id: planId })
  });
  const data = await res.json();

  if (data.status === "success") {
    currentCheckoutRef = data.reference;
    document.getElementById("modalPlanTitle").textContent = "Activate " + data.plan_name;
    document.getElementById("modalAmountDisplay").textContent = "₦" + Number(data.amount_ngn).toLocaleString();
    
    if (data.producer_account) {
      document.getElementById("modalBankName").textContent = data.producer_account.bank_name;
      document.getElementById("modalAccountNumber").textContent = data.producer_account.account_number;
      document.getElementById("modalAccountName").textContent = data.producer_account.account_name;
      
      const waNum = (data.producer_account.whatsapp_phone || "2348091977795").replace("+", "").replace(/\s+/g, "");
      const waMsg = encodeURIComponent(`Hello Manifest! 🎯

I want to activate PassMaster AI: ${data.plan_name} (₦${Number(data.amount_ngn).toLocaleString()}).
• Candidate: ${candidateName}
• Ref ID: ${data.reference}

I am transferring now. Kindly confirm!`);
      document.getElementById("modalWhatsAppBtn").href = "https://wa.me/" + waNum + "?text=" + waMsg;
    }
    document.getElementById("modalRefDisplay").textContent = data.reference;
    modal.classList.add("active");
  }
}

function copyAccountToClipboard() {
  const num = document.getElementById("modalAccountNumber").textContent.trim();
  navigator.clipboard.writeText(num);
  alert("📋 Account Number copied to clipboard: " + num);
}

async function submitPaymentOrder() {
  try {
    const res = await fetch("/api/payments/submit-transfer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        plan_id: activePlan || "monthly",
        reference: currentCheckoutRef,
        name: candidateName
      })
    });
    const d = await res.json();
    if (d.status === "order_created") {
      alert(`✅ Payment order logged with Ref ID: ${d.reference}

Click OK to open WhatsApp and send your transfer receipt to the Producer for instant activation!`);
      window.open(d.whatsapp_url, "_blank");
      closeModal("paymentModal");
    }
  } catch (err) {
    alert("Error submitting payment: " + err);
  }
}

async function redeemVoucher() {
  const pin = document.getElementById("voucherInput").value.trim();
  if (!pin) {
    alert("Please enter a voucher PIN");
    return;
  }
  const res = await fetch("/api/payments/redeem-voucher", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ pin_code: pin })
  });
  const data = await res.json();
  if (data.status === "success") {
    alert("🎉 " + data.message);
    document.getElementById("voucherInput").value = "";
    checkAuth();
    switchView("cbt");
  } else {
    alert("❌ " + data.error);
  }
}

async function openShareModal() {
  const res = await fetch("/api/diagnostics/share-card", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: candidateName,
      course: targetCourse,
      university: targetUni,
      history: sessionHistory,
      cheat_count: antiCheatSwitchCount
    })
  });
  const data = await res.json();
  document.getElementById("shareCardPreview").textContent = data.card_text;
  document.getElementById("shareModal").classList.add("active");
}

function copyShareCard() {
  const text = document.getElementById("shareCardPreview").textContent;
  navigator.clipboard.writeText(text).then(() => {
    alert("🎉 Scorecard copied to clipboard! Paste it directly into your WhatsApp status or study group.");
    closeModal("shareModal");
  }).catch(() => {
    alert("Copied text: " + text);
    closeModal("shareModal");
  });
}

// ----------------- FOUNDER SUPPORT MODAL -----------------
async function openSupportModal() {
  try {
    const res = await fetch("/api/support/bio");
    const data = await res.json();
    if (data.bio) {
      const bioElem = document.getElementById("supportBioDisplay");
      if (bioElem) bioElem.textContent = data.bio;
    }
  } catch (e) {
    console.log("Using default founder story.");
  }
  openModal("supportModal");
}

function copySupportAccount() {
  const acc = document.getElementById("supportAccNum").textContent.trim();
  navigator.clipboard.writeText(acc).then(() => {
    alert("📋 Manifest's First Bank account number copied to clipboard: " + acc);
  }).catch(() => {
    alert("Account Number: " + acc);
  });
}

// ----------------- COUNTDOWN TIMER (JAMB 2026/2027) -----------------
function startExamCountdown() {
  // Targeting JAMB UTME April 17, 2027 08:00:00 WAT
  const targetDate = new Date("2027-04-17T08:00:00+01:00").getTime();

  setInterval(() => {
    const now = new Date().getTime();
    const distance = targetDate - now;

    if (distance <= 0) {
      const elem = document.getElementById("examCountdownDisplay");
      if (elem) elem.textContent = "JAMB Examination Session Active!";
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    const elem = document.getElementById("examCountdownDisplay");
    if (elem) {
      elem.textContent = `${days}d : ${String(hours).padStart(2, "0")}h : ${String(minutes).padStart(2, "0")}m : ${String(seconds).padStart(2, "0")}s`;
    }
  }, 1000);
}


// ----------------- CBT SUBJECT TABS & NAVIGATION -----------------
function getSubjectIcon(subj) {
  const s = (subj || "").toLowerCase();
  if (s.includes("english")) return "📖";
  if (s.includes("math")) return "📐";
  if (s.includes("physic")) return "⚡";
  if (s.includes("chem")) return "🧪";
  if (s.includes("bio")) return "🧬";
  if (s.includes("econ")) return "📊";
  if (s.includes("gov")) return "🏛️";
  if (s.includes("lit")) return "🎭";
  return "📝";
}

function renderCbtSubjectTabs() {
  const container = document.getElementById("cbtSubjectTabsContainer");
  if (!container || !filteredQuestions || filteredQuestions.length === 0) return;

  const subjects = [];
  filteredQuestions.forEach(q => {
    if (!subjects.includes(q.subject)) subjects.push(q.subject);
  });

  const currentQ = filteredQuestions[currentIndex];
  const currentSubj = currentQ ? currentQ.subject : subjects[0];

  container.innerHTML = "";
  subjects.forEach(subj => {
    const totalCount = filteredQuestions.filter(q => q.subject === subj).length;
    const answeredCount = filteredQuestions.filter(q => q.subject === subj && sessionHistory[q.id]).length;
    const isActive = (currentSubj === subj);
    const isCompleted = (totalCount > 0 && answeredCount === totalCount);

    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = `cbt-subject-tab ${isActive ? "active" : ""} ${isCompleted ? "completed" : ""}`;
    btn.innerHTML = `
      <span>${getSubjectIcon(subj)} ${subj}</span>
      <span class="badge-count">${isCompleted ? "✓ " : ""}${answeredCount}/${totalCount}</span>
    `;
    btn.onclick = () => jumpToSubject(subj);
    container.appendChild(btn);
  });
}

function jumpToSubject(subj) {
  if (!filteredQuestions || filteredQuestions.length === 0) return;
  const idx = filteredQuestions.findIndex(q => q.subject.toLowerCase() === subj.toLowerCase());
  if (idx !== -1) {
    currentIndex = idx;
    currentActiveSubject = subj;
    renderCurrentQuestion();
    renderPaletteGrid();
    renderCbtSubjectTabs();
  }
}


// ----------------- EDUCATIONAL SVG SCHEMATICS ENGINE -----------------
function getTopicDiagramSvg(subject, topic) {
  const s = (subject || "").toLowerCase();
  const t = (topic || "").toLowerCase();

  // 1. BIOLOGY
  if (s.includes("bio")) {
    if (t.includes("cell")) {
      return {
        title: "Eukaryotic Cell Ultrastructure & Organelles",
        svg: `<svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="cellGrad" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#0f2b3e" />
              <stop offset="100%" stop-color="#071520" />
            </radialGradient>
            <radialGradient id="nucGrad" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9" />
              <stop offset="100%" stop-color="#0284c7" stop-opacity="0.95" />
            </radialGradient>
          </defs>
          <!-- Cell Membrane -->
          <ellipse cx="260" cy="140" rx="220" ry="115" fill="url(#cellGrad)" stroke="#38bdf8" stroke-width="3.5" />
          <!-- Cytoplasm Label -->
          <text x="70" y="55" fill="#94a3b8" font-size="11" font-weight="700">CYTOPLASM (Cytosol)</text>
          <!-- Nucleus -->
          <ellipse cx="230" cy="135" rx="55" ry="45" fill="url(#nucGrad)" stroke="#bae6fd" stroke-width="2" />
          <circle cx="230" cy="135" r="18" fill="#0369a1" stroke="#e0f2fe" stroke-width="1.5" />
          <text x="195" y="140" fill="#ffffff" font-size="10" font-weight="bold">Nucleolus</text>
          <!-- Mitochondria (Powerhouse) -->
          <g transform="translate(360, 80) rotate(25)">
            <ellipse cx="0" cy="0" rx="35" ry="16" fill="#b91c1c" stroke="#f87171" stroke-width="1.5" />
            <path d="M -22 0 Q -10 -10 0 0 T 22 0" fill="none" stroke="#fef08a" stroke-width="2" />
            <text x="-25" y="28" fill="#fca5a5" font-size="9" font-weight="bold">Mitochondrion (ATP)</text>
          </g>
          <!-- Ribosomes / ER -->
          <g transform="translate(130, 165)">
            <path d="M 0 0 C 20 -15, 30 15, 50 0 C 70 -15, 80 15, 100 0" fill="none" stroke="#a855f7" stroke-width="3" />
            <circle cx="20" cy="-6" r="2.5" fill="#e9d5ff" />
            <circle cx="50" cy="0" r="2.5" fill="#e9d5ff" />
            <circle cx="75" cy="-6" r="2.5" fill="#e9d5ff" />
            <text x="0" y="22" fill="#d8b4fe" font-size="9" font-weight="bold">Rough ER + Ribosomes</text>
          </g>
          <!-- Cell Membrane Label -->
          <line x1="390" y1="210" x2="440" y2="235" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" />
          <text x="400" y="250" fill="#38bdf8" font-size="10" font-weight="bold">Cell Membrane (Phospholipid Bilayer)</text>
        </svg>`,
        legend: [
          { color: "#38bdf8", label: "Plasma Membrane & Nucleus" },
          { color: "#f87171", label: "Mitochondria (ATP Cellular Respiration)" },
          { color: "#c084fc", label: "Rough ER (Protein Synthesis)" }
        ]
      };
    } else if (t.includes("circulat") || t.includes("transport")) {
      return {
        title: "Mammalian Heart 4-Chamber Blood Flow",
        svg: `<svg viewBox="0 0 540 260" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <!-- Heart outline -->
          <rect x="140" y="30" width="260" height="200" rx="30" fill="#0f172a" stroke="#475569" stroke-width="3" />
          <line x1="270" y1="30" x2="270" y2="230" stroke="#64748b" stroke-width="4" />
          <line x1="140" y1="130" x2="400" y2="130" stroke="#64748b" stroke-width="3" />
          <!-- Right Side (Deoxygenated - Blue) -->
          <rect x="150" y="40" width="110" height="80" rx="8" fill="rgba(37, 99, 235, 0.25)" />
          <text x="165" y="75" fill="#60a5fa" font-size="12" font-weight="bold">Right Atrium</text>
          <text x="165" y="95" fill="#93c5fd" font-size="9">(Vena Cava Inflow)</text>
          <rect x="150" y="140" width="110" height="80" rx="8" fill="rgba(37, 99, 235, 0.4)" />
          <text x="158" y="175" fill="#60a5fa" font-size="12" font-weight="bold">Right Ventricle</text>
          <text x="158" y="195" fill="#93c5fd" font-size="9">Pumps to Lungs (Pulm. Art.)</text>
          <!-- Left Side (Oxygenated - Red) -->
          <rect x="280" y="40" width="110" height="80" rx="8" fill="rgba(239, 68, 68, 0.25)" />
          <text x="298" y="75" fill="#f87171" font-size="12" font-weight="bold">Left Atrium</text>
          <text x="292" y="95" fill="#fca5a5" font-size="9">(Pulm. Veins Inflow)</text>
          <rect x="280" y="140" width="110" height="80" rx="8" fill="rgba(239, 68, 68, 0.45)" />
          <text x="295" y="175" fill="#f87171" font-size="12" font-weight="bold">Left Ventricle</text>
          <text x="290" y="195" fill="#fca5a5" font-size="9">Thickest Muscle → Aorta</text>
          <!-- Flow Arrows -->
          <text x="35" y="85" fill="#38bdf8" font-size="10" font-weight="bold">From Body →</text>
          <text x="420" y="190" fill="#f87171" font-size="10" font-weight="bold">→ To Systemic Body (Aorta)</text>
        </svg>`,
        legend: [
          { color: "#3b82f6", label: "Deoxygenated Blood (Right chambers & Pulmonary Artery)" },
          { color: "#ef4444", label: "Oxygenated Blood (Left chambers & Aorta)" }
        ]
      };
    } else if (t.includes("genetics") || t.includes("heredity")) {
      return {
        title: "Monohybrid Cross (Punnett Square) & Mendelian Ratios",
        svg: `<svg viewBox="0 0 540 250" width="100%" height="230" xmlns="http://www.w3.org/2000/svg">
          <text x="180" y="30" fill="#38bdf8" font-size="14" font-weight="bold">Parent Cross: Bb (Heterozygous) × Bb</text>
          <!-- Gametes -->
          <text x="260" y="65" fill="#fbbf24" font-size="14" font-weight="bold">B</text>
          <text x="360" y="65" fill="#fbbf24" font-size="14" font-weight="bold">b</text>
          <text x="185" y="115" fill="#fbbf24" font-size="14" font-weight="bold">B</text>
          <text x="185" y="185" fill="#fbbf24" font-size="14" font-weight="bold">b</text>
          <!-- Grid -->
          <rect x="220" y="80" width="100" height="60" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2" />
          <text x="255" y="118" fill="#34d399" font-size="16" font-weight="bold">BB</text>
          <rect x="320" y="80" width="100" height="60" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="2" />
          <text x="355" y="118" fill="#7dd3fc" font-size="16" font-weight="bold">Bb</text>
          <rect x="220" y="140" width="100" height="60" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="2" />
          <text x="255" y="178" fill="#7dd3fc" font-size="16" font-weight="bold">Bb</text>
          <rect x="320" y="140" width="100" height="60" fill="rgba(239, 68, 68, 0.2)" stroke="#ef4444" stroke-width="2" />
          <text x="355" y="178" fill="#fca5a5" font-size="16" font-weight="bold">bb</text>
          <!-- Ratios -->
          <text x="140" y="230" fill="#ffffff" font-size="12" font-weight="bold">Phenotypic Ratio = 3 Dominant : 1 Recessive (75% : 25%)</text>
        </svg>`,
        legend: [
          { color: "#10b981", label: "Homozygous Dominant (BB - 25%)" },
          { color: "#38bdf8", label: "Heterozygous Carrier (Bb - 50%)" },
          { color: "#ef4444", label: "Homozygous Recessive (bb - 25%)" }
        ]
      };
    } else {
      // Ecology
      return {
        title: "Trophic Energy Flow Pyramid (10% Rule)",
        svg: `<svg viewBox="0 0 540 240" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
          <!-- Pyramid Tiers -->
          <polygon points="270,30 220,80 320,80" fill="rgba(239, 68, 68, 0.5)" stroke="#ef4444" stroke-width="2" />
          <text x="245" y="65" fill="#ffffff" font-size="10" font-weight="bold">Apex (10 J)</text>
          <polygon points="220,80 170,130 370,130 320,80" fill="rgba(251, 191, 36, 0.45)" stroke="#fbbf24" stroke-width="2" />
          <text x="205" y="112" fill="#ffffff" font-size="11" font-weight="bold">Secondary Consumers (100 J)</text>
          <polygon points="170,130 110,185 430,185 370,130" fill="rgba(56, 189, 248, 0.45)" stroke="#38bdf8" stroke-width="2" />
          <text x="185" y="165" fill="#ffffff" font-size="11" font-weight="bold">Primary Herbivores (1,000 J)</text>
          <polygon points="110,185 40,230 500,230 430,185" fill="rgba(16, 185, 129, 0.55)" stroke="#10b981" stroke-width="2" />
          <text x="175" y="215" fill="#ffffff" font-size="12" font-weight="bold">Primary Producers / Plants (10,000 J)</text>
          <!-- 10% Label -->
          <text x="390" y="55" fill="#f87171" font-size="10" font-weight="bold">90% Energy Lost as Heat</text>
        </svg>`,
        legend: [
          { color: "#10b981", label: "Producers (Solar Energy Trappers)" },
          { color: "#38bdf8", label: "Herbivores" },
          { color: "#fbbf24", label: "Carnivores" },
          { color: "#ef4444", label: "Apex Predators" }
        ]
      };
    }
  }

  // 2. PHYSICS
  if (s.includes("physic")) {
    if (t.includes("project") || t.includes("motion") || t.includes("vector")) {
      return {
        title: "Parabolic Projectile Trajectory & Velocity Decomposition",
        svg: `<svg viewBox="0 0 540 250" width="100%" height="230" xmlns="http://www.w3.org/2000/svg">
          <!-- Axes -->
          <line x1="50" y1="210" x2="500" y2="210" stroke="#64748b" stroke-width="2" />
          <line x1="50" y1="210" x2="50" y2="30" stroke="#64748b" stroke-width="2" />
          <text x="505" y="215" fill="#94a3b8" font-size="11">X (Range)</text>
          <text x="35" y="25" fill="#94a3b8" font-size="11">Y</text>
          <!-- Parabola path -->
          <path d="M 50 210 Q 250 -30 450 210" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4" />
          <!-- Initial Vector -->
          <line x1="50" y1="210" x2="120" y2="135" stroke="#f59e0b" stroke-width="3" />
          <polygon points="120,135 110,145 125,148" fill="#f59e0b" />
          <text x="125" y="130" fill="#fbbf24" font-size="12" font-weight="bold">v₀ (Launch)</text>
          <text x="75" y="195" fill="#fbbf24" font-size="10">θ</text>
          <!-- Apex H max -->
          <circle cx="250" cy="90" r="5" fill="#ef4444" />
          <line x1="250" y1="90" x2="250" y2="210" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3" />
          <text x="258" y="145" fill="#fca5a5" font-size="11" font-weight="bold">H_max = (v₀² sin²θ)/(2g)</text>
          <text x="210" y="80" fill="#ffffff" font-size="10" font-weight="bold">Apex: v_y = 0</text>
          <!-- Range -->
          <text x="210" y="235" fill="#38bdf8" font-size="11" font-weight="bold">Range R = (v₀² sin 2θ)/g</text>
        </svg>`,
        legend: [
          { color: "#f59e0b", label: "Initial Velocity Vector (v₀) & Angle θ" },
          { color: "#38bdf8", label: "Horizontal Motion (Constant v_x = v₀ cosθ)" },
          { color: "#ef4444", label: "Vertical Deceleration (a_y = -g)" }
        ]
      };
    } else if (t.includes("circuit") || t.includes("cell") || t.includes("current")) {
      return {
        title: "DC Circuit Schematic: EMF (E), Internal Resistance (r) & Load (R)",
        svg: `<svg viewBox="0 0 540 230" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
          <!-- Wire loop -->
          <rect x="70" y="40" width="400" height="150" fill="none" stroke="#38bdf8" stroke-width="3" rx="10" />
          <!-- Battery with EMF & internal resistance -->
          <rect x="180" y="30" width="160" height="30" fill="#0b1329" stroke="#64748b" stroke-width="1.5" />
          <!-- Long and short cell lines -->
          <line x1="210" y1="35" x2="210" y2="55" stroke="#10b981" stroke-width="4" />
          <line x1="225" y1="40" x2="225" y2="50" stroke="#ef4444" stroke-width="2" />
          <text x="195" y="25" fill="#10b981" font-size="11" font-weight="bold">+ E (EMF) -</text>
          <!-- Internal resistance zigzag -->
          <path d="M 245 45 L 255 35 L 265 55 L 275 35 L 285 55 L 295 45" fill="none" stroke="#fbbf24" stroke-width="2.5" />
          <text x="260" y="25" fill="#fbbf24" font-size="10" font-weight="bold">r (internal)</text>
          <!-- External Resistor R -->
          <rect x="220" y="178" width="80" height="24" fill="#1e293b" stroke="#f43f5e" stroke-width="2" />
          <text x="235" y="195" fill="#f43f5e" font-size="12" font-weight="bold">Load R</text>
          <!-- Formula -->
          <text x="150" y="125" fill="#ffffff" font-size="13" font-weight="bold">Total Current I = E / (R + r)</text>
          <text x="135" y="145" fill="#93c5fd" font-size="11">Terminal Voltage V = E - Ir = IR</text>
        </svg>`,
        legend: [
          { color: "#10b981", label: "Electromotive Force (E in Volts)" },
          { color: "#fbbf24", label: "Internal Resistance (r in Ohms)" },
          { color: "#f43f5e", label: "External Load (R in Ohms)" }
        ]
      };
    } else {
      // Wave mechanics
      return {
        title: "Transverse Wave Anatomy: Wavelength, Amplitude & Nodes",
        svg: `<svg viewBox="0 0 540 230" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
          <!-- Baseline -->
          <line x1="40" y1="115" x2="500" y2="115" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4" />
          <!-- Sinusoid -->
          <path d="M 50 115 Q 110 25 170 115 T 290 115 T 410 115 T 490 115" fill="none" stroke="#38bdf8" stroke-width="3.5" />
          <!-- Amplitude arrow -->
          <line x1="110" y1="115" x2="110" y2="35" stroke="#10b981" stroke-width="2" />
          <text x="118" y="75" fill="#10b981" font-size="11" font-weight="bold">Amplitude (A)</text>
          <!-- Crest and trough -->
          <text x="95" y="25" fill="#38bdf8" font-size="11" font-weight="bold">Crest</text>
          <text x="215" y="210" fill="#fca5a5" font-size="11" font-weight="bold">Trough</text>
          <!-- Wavelength bracket -->
          <line x1="110" y1="20" x2="350" y2="20" stroke="#fbbf24" stroke-width="2" />
          <text x="200" y="15" fill="#fbbf24" font-size="11" font-weight="bold">Wavelength (λ)</text>
          <!-- Formula -->
          <text x="180" y="155" fill="#ffffff" font-size="13" font-weight="bold">Wave Speed Equation: v = f × λ</text>
        </svg>`,
        legend: [
          { color: "#fbbf24", label: "Wavelength λ (Distance between consecutive crests)" },
          { color: "#10b981", label: "Amplitude A (Max displacement from baseline)" },
          { color: "#38bdf8", label: "Wave Speed v = fλ" }
        ]
      };
    }
  }

  // 3. CHEMISTRY
  if (s.includes("chem")) {
    if (t.includes("energetics") || t.includes("thermo") || t.includes("rate")) {
      return {
        title: "Reaction Coordinate Energy Profile (Exothermic vs Catalyst)",
        svg: `<svg viewBox="0 0 540 240" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
          <!-- Axes -->
          <line x1="60" y1="210" x2="480" y2="210" stroke="#64748b" stroke-width="2" />
          <line x1="60" y1="210" x2="60" y2="30" stroke="#64748b" stroke-width="2" />
          <text x="400" y="230" fill="#94a3b8" font-size="11">Reaction Coordinate →</text>
          <text x="20" y="25" fill="#94a3b8" font-size="11">Potential Energy (kJ)</text>
          <!-- Reactants -->
          <line x1="60" y1="120" x2="130" y2="120" stroke="#10b981" stroke-width="3.5" />
          <text x="70" y="110" fill="#10b981" font-size="11" font-weight="bold">Reactants</text>
          <!-- Uncatalyzed barrier -->
          <path d="M 130 120 Q 230 -20 330 170" fill="none" stroke="#ef4444" stroke-width="3" />
          <text x="205" y="25" fill="#ef4444" font-size="10" font-weight="bold">Ea (Uncatalyzed)</text>
          <!-- Catalyzed barrier -->
          <path d="M 130 120 Q 230 40 330 170" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="5,4" />
          <text x="245" y="70" fill="#38bdf8" font-size="10" font-weight="bold">Ea (With Catalyst)</text>
          <!-- Products -->
          <line x1="330" y1="170" x2="440" y2="170" stroke="#fbbf24" stroke-width="3.5" />
          <text x="350" y="195" fill="#fbbf24" font-size="11" font-weight="bold">Products</text>
          <!-- ΔH -->
          <line x1="430" y1="120" x2="430" y2="170" stroke="#f43f5e" stroke-width="2" />
          <text x="440" y="150" fill="#f43f5e" font-size="11" font-weight="bold">ΔH &lt; 0 (Exothermic)</text>
        </svg>`,
        legend: [
          { color: "#ef4444", label: "Activation Energy Barrier (Ea)" },
          { color: "#38bdf8", label: "Catalyzed Pathway (Lower Ea, Faster Rate)" },
          { color: "#f43f5e", label: "Enthalpy Change ΔH = H_products - H_reactants" }
        ]
      };
    } else {
      // Periodic trends
      return {
        title: "Periodic Table Periodic Trends Coordinate Map",
        svg: `<svg viewBox="0 0 540 230" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
          <!-- Table outline -->
          <path d="M 70 80 L 140 80 L 140 120 L 350 120 L 350 50 L 460 50 L 460 190 L 70 190 Z" fill="rgba(30, 41, 59, 0.7)" stroke="#64748b" stroke-width="2" />
          <!-- Arrow: Electronegativity & Ionization Energy -->
          <line x1="70" y1="35" x2="450" y2="35" stroke="#38bdf8" stroke-width="3" />
          <polygon points="450,35 440,30 440,40" fill="#38bdf8" />
          <text x="140" y="25" fill="#38bdf8" font-size="11" font-weight="bold">Electronegativity &amp; Ionization Energy Increase →</text>
          <!-- Arrow: Atomic Radius -->
          <line x1="475" y1="60" x2="475" y2="185" stroke="#ef4444" stroke-width="3" />
          <polygon points="475,185 470,175 480,175" fill="#ef4444" />
          <text x="280" y="215" fill="#fca5a5" font-size="11" font-weight="bold">Atomic Radius Increases Downwards &amp; Leftwards ↙</text>
          <!-- Central Note -->
          <text x="175" y="160" fill="#ffffff" font-size="12" font-weight="bold">Fluorine (F) = Highest Electronegativity</text>
        </svg>`,
        legend: [
          { color: "#38bdf8", label: "Electronegativity & Ionization Energy (Increases Across Period)" },
          { color: "#ef4444", label: "Atomic Radius (Increases Down Group due to extra shells)" }
        ]
      };
    }
  }

  // 4. MATHEMATICS
  if (s.includes("math")) {
    if (t.includes("calculus") || t.includes("differentiation") || t.includes("integration")) {
      return {
        title: "Calculus: Tangent Slope (dy/dx) & Definite Integral Area",
        svg: `<svg viewBox="0 0 540 240" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
          <!-- Axes -->
          <line x1="50" y1="210" x2="480" y2="210" stroke="#64748b" stroke-width="2" />
          <line x1="50" y1="210" x2="50" y2="30" stroke="#64748b" stroke-width="2" />
          <!-- Shaded Area Under Curve -->
          <path d="M 140 210 L 140 160 Q 230 60 340 110 L 340 210 Z" fill="rgba(56, 189, 248, 0.25)" stroke="none" />
          <text x="210" y="175" fill="#38bdf8" font-size="12" font-weight="bold">Area = ∫ a to b f(x) dx</text>
          <!-- Curve -->
          <path d="M 70 200 Q 200 40 430 100" fill="none" stroke="#ffffff" stroke-width="3" />
          <text x="390" y="80" fill="#ffffff" font-size="12" font-weight="bold">y = f(x)</text>
          <!-- Tangent Line -->
          <line x1="170" y1="175" x2="310" y2="65" stroke="#f59e0b" stroke-width="2.5" />
          <circle cx="240" cy="120" r="5" fill="#f59e0b" />
          <text x="250" y="115" fill="#fbbf24" font-size="11" font-weight="bold">Slope = dy/dx = f'(x)</text>
        </svg>`,
        legend: [
          { color: "#f59e0b", label: "Differentiation: Instantaneous Rate of Change (Slope)" },
          { color: "#38bdf8", label: "Integration: Continuous Summation (Area under Curve)" }
        ]
      };
    } else {
      // Quadratic / Coordinate
      return {
        title: "Quadratic Parabola Anatomy & Roots (b² - 4ac)",
        svg: `<svg viewBox="0 0 540 230" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
          <!-- Axes -->
          <line x1="50" y1="160" x2="480" y2="160" stroke="#64748b" stroke-width="2" />
          <line x1="260" y1="210" x2="260" y2="20" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3" />
          <text x="268" y="40" fill="#94a3b8" font-size="10">Axis of Symmetry: x = -b/(2a)</text>
          <!-- Parabola curve -->
          <path d="M 120 40 Q 260 260 400 40" fill="none" stroke="#10b981" stroke-width="3.5" />
          <!-- Roots -->
          <circle cx="178" cy="160" r="5" fill="#ef4444" />
          <text x="160" y="150" fill="#fca5a5" font-size="11" font-weight="bold">Root x₁</text>
          <circle cx="342" cy="160" r="5" fill="#ef4444" />
          <text x="345" y="150" fill="#fca5a5" font-size="11" font-weight="bold">Root x₂</text>
          <!-- Vertex -->
          <circle cx="260" cy="195" r="5" fill="#38bdf8" />
          <text x="270" y="200" fill="#38bdf8" font-size="11" font-weight="bold">Minimum Vertex (h, k)</text>
          <text x="140" y="220" fill="#ffffff" font-size="11" font-weight="bold">Discriminant Δ = b² - 4ac &gt; 0 (Two Real Distinct Roots)</text>
        </svg>`,
        legend: [
          { color: "#10b981", label: "Parabola Curve y = ax² + bx + c" },
          { color: "#ef4444", label: "Real Roots (x-intercepts where y = 0)" },
          { color: "#38bdf8", label: "Vertex Extremum" }
        ]
      };
    }
  }

  // 5. ECONOMICS
  if (s.includes("econ")) {
    return {
      title: "Marshallian Market Equilibrium: Supply & Demand",
      svg: `<svg viewBox="0 0 540 230" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
        <!-- Axes -->
        <line x1="70" y1="190" x2="470" y2="190" stroke="#64748b" stroke-width="2" />
        <line x1="70" y1="190" x2="70" y2="30" stroke="#64748b" stroke-width="2" />
        <text x="430" y="210" fill="#94a3b8" font-size="11">Quantity (Q)</text>
        <text x="25" y="35" fill="#94a3b8" font-size="11">Price (P)</text>
        <!-- Demand Curve (Downward sloping) -->
        <line x1="110" y1="50" x2="430" y2="175" stroke="#ef4444" stroke-width="3" />
        <text x="435" y="180" fill="#ef4444" font-size="12" font-weight="bold">Demand (D)</text>
        <!-- Supply Curve (Upward sloping) -->
        <line x1="110" y1="175" x2="430" y2="50" stroke="#10b981" stroke-width="3" />
        <text x="435" y="55" fill="#10b981" font-size="12" font-weight="bold">Supply (S)</text>
        <!-- Equilibrium point -->
        <circle cx="270" cy="112" r="6" fill="#fbbf24" />
        <line x1="70" y1="112" x2="270" y2="112" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,3" />
        <line x1="270" y1="112" x2="270" y2="190" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,3" />
        <text x="280" y="105" fill="#fbbf24" font-size="12" font-weight="bold">Equilibrium (P*, Q*)</text>
        <text x="80" y="105" fill="#fbbf24" font-size="10">P*</text>
        <text x="265" y="205" fill="#fbbf24" font-size="10">Q*</text>
      </svg>`,
      legend: [
        { color: "#ef4444", label: "Demand (Law of Demand: Higher Price → Lower Quantity)" },
        { color: "#10b981", label: "Supply (Law of Supply: Higher Price → Higher Quantity)" },
        { color: "#fbbf24", label: "Market Clearing Price & Quantity" }
      ]
    };
  }

  // 6. GOVERNMENT
  if (s.includes("gov")) {
    return {
      title: "Tripartite Separation of Powers & Constitutional Checks",
      svg: `<svg viewBox="0 0 540 230" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
        <!-- Executive -->
        <rect x="50" y="40" width="120" height="70" rx="8" fill="rgba(37, 99, 235, 0.3)" stroke="#3b82f6" stroke-width="2" />
        <text x="75" y="70" fill="#60a5fa" font-size="12" font-weight="bold">EXECUTIVE</text>
        <text x="65" y="90" fill="#93c5fd" font-size="9">Enforces Laws</text>
        <!-- Legislature -->
        <rect x="370" y="40" width="120" height="70" rx="8" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="2" />
        <text x="385" y="70" fill="#34d399" font-size="12" font-weight="bold">LEGISLATURE</text>
        <text x="390" y="90" fill="#a7f3d0" font-size="9">Enacts Laws</text>
        <!-- Judiciary -->
        <rect x="210" y="145" width="120" height="70" rx="8" fill="rgba(245, 158, 11, 0.3)" stroke="#f59e0b" stroke-width="2" />
        <text x="235" y="175" fill="#fbbf24" font-size="12" font-weight="bold">JUDICIARY</text>
        <text x="225" y="195" fill="#fef08a" font-size="9">Interprets Laws</text>
        <!-- Interconnecting arrows -->
        <line x1="170" y1="75" x2="370" y2="75" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,3" />
        <text x="230" y="68" fill="#cbd5e1" font-size="9">Veto &amp; Budget</text>
        <line x1="110" y1="110" x2="210" y2="165" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,3" />
        <line x1="430" y1="110" x2="330" y2="165" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,3" />
        <text x="145" y="225" fill="#38bdf8" font-size="10" font-weight="bold">Constitutional System of Checks &amp; Balances</text>
      </svg>`,
      legend: [
        { color: "#3b82f6", label: "Executive (President, Governors, Ministers)" },
        { color: "#10b981", label: "Legislature (Senate, House of Representatives)" },
        { color: "#f59e0b", label: "Judiciary (Supreme Court, Judicial Review)" }
      ]
    };
  }

  // 7. DEFAULT / USE OF ENGLISH & LITERATURE
  return {
    title: "Syllabus Conceptual Relationship & Decision Model",
    svg: `<svg viewBox="0 0 540 210" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
      <rect x="40" y="40" width="130" height="60" rx="8" fill="rgba(56, 189, 248, 0.25)" stroke="#38bdf8" stroke-width="2" />
      <text x="60" y="75" fill="#7dd3fc" font-size="12" font-weight="bold">Foundations</text>
      <line x1="170" y1="70" x2="215" y2="70" stroke="#94a3b8" stroke-width="2.5" />
      <polygon points="215,70 205,65 205,75" fill="#94a3b8" />
      <rect x="220" y="40" width="130" height="60" rx="8" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2" />
      <text x="240" y="75" fill="#6ee7b7" font-size="12" font-weight="bold">Core Axioms</text>
      <line x1="350" y1="70" x2="395" y2="70" stroke="#94a3b8" stroke-width="2.5" />
      <polygon points="395,70 385,65 385,75" fill="#94a3b8" />
      <rect x="400" y="40" width="110" height="60" rx="8" fill="rgba(245, 158, 11, 0.25)" stroke="#f59e0b" stroke-width="2" />
      <text x="415" y="75" fill="#fde68a" font-size="12" font-weight="bold">JAMB Mastery</text>
      <text x="120" y="150" fill="#ffffff" font-size="12" font-weight="bold">Rule Hierarchy: Zero Exceptions when applied in standard order</text>
      <text x="100" y="175" fill="#94a3b8" font-size="11">Always isolate core modifiers before evaluating predicate options.</text>
    </svg>`,
    legend: [
      { color: "#38bdf8", label: "Fundamental Definitions" },
      { color: "#10b981", label: "Structural Rules" },
      { color: "#f59e0b", label: "Exam Application Heuristics" }
    ]
  };
}

function renderTopicVisual(subject, topic) {
  const mount = document.getElementById("lessonDiagramMount");
  const legend = document.getElementById("lessonDiagramLegend");
  const title = document.getElementById("lessonDiagramTitle");
  if (!mount) return;

  const data = getTopicDiagramSvg(subject, topic);
  mount.innerHTML = data.svg;
  if (title) title.textContent = data.title;

  if (legend) {
    legend.innerHTML = "";
    (data.legend || []).forEach(item => {
      const d = document.createElement("div");
      d.className = "diagram-legend-item";
      d.innerHTML = `<span class="diagram-legend-dot" style="background: ${item.color};"></span><span>${item.label}</span>`;
      legend.appendChild(d);
    });
  }
}


// ----------------- VIDEO LECTURE THEATER SIMULATION -----------------
let simulatedVideoPlaying = false;
let simulatedVideoTimer = null;
let simulatedVideoSeconds = 0;
let simulatedVideoDuration = 1000; // 16:40 in seconds
let simulatedVideoSpeed = 1.0;

function renderTopicVideo(videoMeta, topicTitle) {
  simulatedVideoPlaying = false;
  clearInterval(simulatedVideoTimer);
  simulatedVideoSeconds = 0;

  const badge = document.getElementById("lessonVideoBadge");
  const lecturer = document.getElementById("lessonVideoLecturer");
  const timer = document.getElementById("lessonVideoTimerDisplay");
  const progress = document.getElementById("lessonVideoProgress");
  const playBtn = document.getElementById("lessonVideoPlayBtn");
  const status = document.getElementById("lessonVideoStatus");
  const waveform = document.getElementById("lessonVideoWaveform");
  const chaptersList = document.getElementById("lessonVideoChaptersList");

  const durationStr = (videoMeta && videoMeta.duration) ? videoMeta.duration : "16:40";
  const parts = durationStr.split(":");
  simulatedVideoDuration = (parseInt(parts[0]) || 16) * 60 + (parseInt(parts[1]) || 40);

  if (badge) badge.textContent = `🎬 JAMB: ${topicTitle}`;
  if (lecturer) lecturer.textContent = (videoMeta && videoMeta.lecturer) ? `👨‍🏫 ${videoMeta.lecturer}` : "PassMaster Socratic Fellow";
  if (timer) timer.textContent = `00:00 / ${durationStr}`;
  if (progress) progress.style.width = "0%";
  if (playBtn) playBtn.textContent = "▶";
  if (status) status.textContent = "Ready to Stream (High-Def)";
  if (waveform) waveform.style.display = "none";

  if (chaptersList) {
    chaptersList.innerHTML = "";
    const chapters = (videoMeta && videoMeta.chapters) ? videoMeta.chapters : [
      { time: "00:00", title: "Zero-to-One Conceptual Foundations" },
      { time: "04:15", title: "Core Laws, Equations & Definitions" },
      { time: "08:30", title: "Authentic JAMB Past Questions Solved" },
      { time: "12:50", title: "Fatal Cognitive Traps & Speed Hacks" }
    ];

    chapters.forEach((ch, idx) => {
      const pill = document.createElement("div");
      pill.className = `video-chapter-pill ${idx === 0 ? "active" : ""}`;
      pill.dataset.time = ch.time;
      pill.innerHTML = `
        <div style="display: flex; align-items: center; gap: 0.5rem;">
          <span style="color: var(--accent-cyan); font-weight: 700;">#${idx + 1}</span>
          <span>${ch.title}</span>
        </div>
        <span style="font-family: monospace; font-size: 0.75rem; color: #94a3b8;">${ch.time}</span>
      `;
      pill.onclick = () => seekToChapter(ch.time, pill);
      chaptersList.appendChild(pill);
    });
  }
}

function toggleSimulatedVideoPlayback() {
  const playBtn = document.getElementById("lessonVideoPlayBtn");
  const status = document.getElementById("lessonVideoStatus");
  const waveform = document.getElementById("lessonVideoWaveform");

  simulatedVideoPlaying = !simulatedVideoPlaying;

  if (simulatedVideoPlaying) {
    if (playBtn) playBtn.textContent = "⏸";
    if (status) status.textContent = "Streaming Live Lecture (Audio & Visuals)";
    if (waveform) waveform.style.display = "flex";

    simulatedVideoTimer = setInterval(() => {
      simulatedVideoSeconds += (1 * simulatedVideoSpeed);
      if (simulatedVideoSeconds >= simulatedVideoDuration) {
        simulatedVideoSeconds = simulatedVideoDuration;
        toggleSimulatedVideoPlayback();
      }
      updateVideoProgressDisplay();
    }, 1000);
  } else {
    clearInterval(simulatedVideoTimer);
    if (playBtn) playBtn.textContent = "▶";
    if (status) status.textContent = "Paused";
    if (waveform) waveform.style.display = "none";
  }
}

function updateVideoProgressDisplay() {
  const timer = document.getElementById("lessonVideoTimerDisplay");
  const progress = document.getElementById("lessonVideoProgress");

  const curM = String(Math.floor(simulatedVideoSeconds / 60)).padStart(2, "0");
  const curS = String(Math.floor(simulatedVideoSeconds % 60)).padStart(2, "0");
  const durM = String(Math.floor(simulatedVideoDuration / 60)).padStart(2, "0");
  const durS = String(Math.floor(simulatedVideoDuration % 60)).padStart(2, "0");

  if (timer) timer.textContent = `${curM}:${curS} / ${durM}:${durS}`;
  if (progress) {
    const pct = Math.min(100, (simulatedVideoSeconds / simulatedVideoDuration) * 100);
    progress.style.width = `${pct}%`;
  }
}

function seekToChapter(timeStr, pillElem) {
  const parts = timeStr.split(":");
  const secs = (parseInt(parts[0]) || 0) * 60 + (parseInt(parts[1]) || 0);
  simulatedVideoSeconds = secs;
  updateVideoProgressDisplay();

  document.querySelectorAll(".video-chapter-pill").forEach(p => p.classList.remove("active"));
  if (pillElem) pillElem.classList.add("active");

  if (!simulatedVideoPlaying) {
    toggleSimulatedVideoPlayback();
  }
}

function seekSimulatedVideo(event) {
  const bar = event.currentTarget;
  const rect = bar.getBoundingClientRect();
  const clickX = event.clientX - rect.left;
  const pct = Math.max(0, Math.min(1, clickX / rect.width));
  simulatedVideoSeconds = Math.floor(pct * simulatedVideoDuration);
  updateVideoProgressDisplay();
}

function setVideoSpeed(spd, elem) {
  simulatedVideoSpeed = parseFloat(spd) || 1.0;
  document.querySelectorAll(".video-speed-pill").forEach(b => b.classList.remove("active"));
  if (elem) elem.classList.add("active");
}


// ----------------- LESSON TABS, WORKED EXAMPLES & PREREQUISITES -----------------
function switchLessonModalTab(tabKey) {
  document.querySelectorAll(".lesson-tab-btn").forEach(b => b.classList.remove("active"));
  const btn = document.getElementById(
    tabKey === 'text' ? 'lessonTabBtnText' :
    tabKey === 'visual' ? 'lessonTabBtnVisual' : 'lessonTabBtnPrereq'
  );
  if (btn) btn.classList.add("active");

  const paneText = document.getElementById("lessonTabPaneText");
  const paneVisual = document.getElementById("lessonTabPaneVisual");
  const panePrereq = document.getElementById("lessonTabPanePrereq");

  if (paneText) paneText.style.display = (tabKey === 'text' ? 'flex' : 'none');
  if (paneVisual) paneVisual.style.display = (tabKey === 'visual' ? 'flex' : 'none');
  if (panePrereq) panePrereq.style.display = (tabKey === 'prereq' ? 'flex' : 'none');
}

function renderWorkedExamples(examples) {
  const container = document.getElementById("lessonWorkedExamplesContainer");
  const box = document.getElementById("lessonWorkedExamplesBox");
  if (!container) return;

  container.innerHTML = "";
  if (!examples || examples.length === 0) {
    if (box) box.style.display = "none";
    return;
  }
  if (box) box.style.display = "block";

  examples.forEach((we, idx) => {
    const card = document.createElement("div");
    card.className = "worked-example-card";

    const optsHtml = (we.options || []).map(opt => `
      <div style="font-size: 0.82rem; color: #cbd5e1; margin-bottom: 0.2rem;">${opt}</div>
    `).join("");

    card.innerHTML = `
      <div class="worked-example-header">
        <span>Authentic JAMB Question #${idx + 1}</span>
        <span style="color: var(--accent-emerald);">Exam Verified</span>
      </div>
      <div style="font-size: 0.88rem; font-weight: 600; color: #ffffff; margin-bottom: 0.5rem; line-height: 1.5;">
        ${we.question}
      </div>
      <div style="margin-left: 0.5rem; margin-bottom: 0.6rem;">
        ${optsHtml}
      </div>
      <div class="worked-example-solution">
        <strong>💡 Step-by-Step Solution & Trap Breakdown:</strong><br>
        ${we.solution}
      </div>
    `;
    container.appendChild(card);
  });
}

function renderPrerequisites(prereqs, preparesFor, subject) {
  const prereqList = document.getElementById("lessonPrereqList");
  const prepList = document.getElementById("lessonPreparesForList");

  if (prereqList) {
    prereqList.innerHTML = "";
    if (!prereqs || prereqs.length === 0) {
      prereqList.innerHTML = `<div style="font-size: 0.82rem; color: var(--text-dim);">No foundational prerequisites required. You can learn this topic directly from first principles!</div>`;
    } else {
      prereqs.forEach(p => {
        const item = document.createElement("div");
        item.style.cssText = "background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: var(--radius-sm); padding: 0.65rem 0.85rem; display: flex; justify-content: space-between; align-items: center; gap: 0.5rem;";
        item.innerHTML = `
          <div>
            <strong style="color: var(--accent-cyan); font-size: 0.85rem;">🌱 ${p.topic}</strong>
            <div style="font-size: 0.76rem; color: var(--text-muted); margin-top: 0.15rem;">${p.reason}</div>
          </div>
          <button class="btn-pill" style="font-size: 0.7rem; padding: 0.25rem 0.65rem; white-space: nowrap;" onclick="viewLesson('${subject.replace(/'/g, "'")}', '${p.topic.replace(/'/g, "'")}', false)">
            📖 Read
          </button>
        `;
        prereqList.appendChild(item);
      });
    }
  }

  if (prepList) {
    prepList.innerHTML = "";
    if (!preparesFor || preparesFor.length === 0) {
      prepList.innerHTML = `<div style="font-size: 0.82rem; color: var(--text-dim);">Provides comprehensive direct scoring weight for official JAMB questions.</div>`;
    } else {
      preparesFor.forEach(topicName => {
        const chip = document.createElement("button");
        chip.type = "button";
        chip.className = "btn-pill";
        chip.style.cssText = "font-size: 0.75rem; padding: 0.3rem 0.65rem;";
        chip.innerHTML = `🚀 ${topicName}`;
        chip.onclick = () => viewLesson(subject, topicName, false);
        prepList.appendChild(chip);
      });
    }
  }
}
