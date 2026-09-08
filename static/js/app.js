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

function openProfileModal() {
  if (!currentUser) {
    openAuthModal('login');
    return;
  }
  const modal = document.getElementById("profileModal");
  if (!modal) return;

  const initial = currentUser.name.charAt(0).toUpperCase();
  document.getElementById("profileAvatarInitial").textContent = initial;
  document.getElementById("profileNameDisplay").textContent = currentUser.name;
  document.getElementById("profileEmailDisplay").textContent = currentUser.email;
  document.getElementById("profilePhoneDisplay").textContent = currentUser.phone || "No phone recorded";
  document.getElementById("profileTargetDisplay").textContent = `${currentUser.target_course} (${currentUser.target_uni})`;
  document.getElementById("profilePlanDisplay").textContent = (currentUser.plan || "Free").toUpperCase() + " TIER";

  const days = currentUser.days_left || 0;
  const hours = (currentUser.hours_left || 0) % 24;
  const daysText = (currentUser.plan && currentUser.plan !== 'free' && days > 0)
    ? `👑 Active Pass: ${days} days, ${hours} hours remaining`
    : "Free Tier (Topic Masterclasses & Full Mocks Locked)";
  document.getElementById("profileDaysLeftText").textContent = daysText;

  modal.classList.add("active");
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
    const res = await fetch("/api/questions?random=true");
    const data = await res.json();
    if (data.status === "success" && data.questions.length > 0) {
      allQuestions = data.questions;
      filteredQuestions = [...allQuestions];
      currentIndex = 0;
      renderCurrentQuestion();
      renderPaletteGrid();
    }
  } catch (err) {
    console.error("Failed to load questions:", err);
  }
}

function filterBySubject(subject, pillElem) {
  document.querySelectorAll(".subject-filter-bar .filter-pill").forEach(p => p.classList.remove("active"));
  if (pillElem) pillElem.classList.add("active");

  if (subject === "all") {
    filteredQuestions = [...allQuestions];
  } else {
    filteredQuestions = allQuestions.filter(q => q.subject.toLowerCase() === subject.toLowerCase());
  }

  currentIndex = 0;
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
  document.getElementById("qCounterDisplay").textContent = "Question " + (currentIndex + 1) + " of " + filteredQuestions.length;

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
  const subj = document.getElementById("setupSubjectSelect").value;
  const topicSelect = document.getElementById("setupTopicSelect");
  if (!topicSelect) return;
  topicSelect.innerHTML = '<option value="">-- All Topics in Subject --</option>';

  if (subj !== 'all' && syllabusData && syllabusData[subj]) {
    syllabusData[subj].topics.forEach(t => {
      const opt = document.createElement("option");
      opt.value = t.name;
      opt.textContent = `${t.name} (${t.weight_pct}% weight)`;
      topicSelect.appendChild(opt);
    });
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
      document.getElementById("lessonSubjectBadge").textContent = les.subject;
      document.getElementById("lessonTopicBadge").textContent = les.topic;
      document.getElementById("lessonModalTitle").textContent = les.title;
      document.getElementById("lessonKeyRule").textContent = les.key_rule_or_formula || "Master this foundational rule.";
      document.getElementById("lessonContentText").textContent = les.content;
      document.getElementById("lessonTrapsText").textContent = les.common_traps || "Watch out for tricky distractors.";
      document.getElementById("lessonTipText").textContent = les.secret_tip || "Eliminate extremes and incorrect units first.";
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
    alert("Failed to load lesson details.");
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
