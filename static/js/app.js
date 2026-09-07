// PassMaster AI — Master Client Engine

let allQuestions = [];
let filteredQuestions = [];
let currentIndex = 0;
let sessionHistory = {};
let timerInterval = null;
let timerSeconds = 40;
let activePlan = null;
let currentUser = null;
let audioEnabled = true;
let sfxEnabled = true;
let flaggedQuestions = new Set();

// Calculator state
let calcCurrent = "0";
let calcPrev = null;
let calcOp = null;

// Candidate Defaults
let candidateName = "Candidate";
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
      osc.frequency.setValueAtTime(523.25, ctx.currentTime); // C5
      osc.frequency.exponentialRampToValueAtTime(659.25, ctx.currentTime + 0.12); // E5
      osc.frequency.exponentialRampToValueAtTime(783.99, ctx.currentTime + 0.25); // G5
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
});

// ----------------- AUTHENTICATION -----------------
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
    const levelName = currentUser.level_name || "Scholar Candidate";
    container.innerHTML = `
      <div style="display: flex; align-items: center; gap: 0.5rem;">
        <span class="streak-badge" title="Consecutive Practice Days">🔥 ${streak} Days</span>
        <span class="streak-badge" style="background: rgba(6, 182, 212, 0.15); color: var(--accent-cyan); border-color: rgba(6, 182, 212, 0.3);">
          ⭐ ${currentUser.xp || 120} XP
        </span>
        <div class="user-profile-badge" onclick="handleLogout()" title="Click to Logout">
          <div class="user-avatar-circle">${initial}</div>
          <span style="font-weight: 600;">${currentUser.name.split(" ")[0]}</span>
          <span style="font-size: 0.7rem; color: var(--text-dim);">⏻</span>
        </div>
      </div>
    `;
  } else {
    container.innerHTML = `
      <button class="btn-pill" onclick="openAuthModal('login')">
        <span>🔐</span>
        <span>Login / Register</span>
      </button>
    `;
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
      alert("👋 Welcome back, " + currentUser.name + "!");
    } else {
      alert("❌ " + data.error);
    }
  } catch (err) {
    alert("Login failed. Check your network.");
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
      alert("🎉 Account created successfully! Your prep journey starts now.");
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
    renderAuthHeader();
    refreshDiagnostics();
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
}

// ----------------- QUESTIONS & CBT SIMULATOR -----------------
async function loadQuestions() {
  try {
    const res = await fetch("/api/questions");
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
  document.querySelectorAll(".filter-pill").forEach(p => p.classList.remove("active"));
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
  if (!window.speechSynthesis || !audioEnabled) return;
  window.speechSynthesis.cancel();
  const clean = text.replace(/[*_#🎯⚠️💡👉📌🔥⚡]/g, "").split(String.fromCharCode(10)).join(". ");
  const utter = new SpeechSynthesisUtterance(clean);
  utter.rate = 1.0;
  utter.pitch = 1.0;
  window.speechSynthesis.speak(utter);
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

// ----------------- SOCRATIC COACH CHAT & AUDIO -----------------
async function handleCoachChatSubmit(e) {
  e.preventDefault();
  const input = document.getElementById("coachMessageInput");
  const msg = input.value.trim();
  if (!msg) return;

  const currentQ = filteredQuestions[currentIndex];
  appendStudentMessage(msg);
  input.value = "";

  try {
    const res = await fetch("/api/tutor/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question_id: currentQ.id, message: msg })
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
  const bubble = document.createElement("div");
  bubble.className = "chat-bubble coach";
  bubble.textContent = text;
  chatArea.appendChild(bubble);
  chatArea.scrollTop = chatArea.scrollHeight;
}

function appendStudentMessage(text) {
  const chatArea = document.getElementById("coachChatArea");
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
async function loadMistakeVault() {
  try {
    const res = await fetch("/api/mistake-vault");
    const data = await res.json();
    const container = document.getElementById("mistakeVaultContainer");
    if (!container) return;

    if (!data.vault || data.vault.length === 0) {
      container.innerHTML = `
        <div style="text-align: center; padding: 2rem; color: var(--text-muted);">
          🎉 <strong>Clean Sheet!</strong> You haven't made any mistakes yet, or you haven't taken a test. Complete questions in CBT mode to log cognitive errors here.
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
        <div class="vault-trap-box">
          ⚠️ <strong>Examiner Trap Explained:</strong> ${m.trap_explanation}
        </div>
        <div style="font-size: 0.8rem; color: var(--accent-emerald); margin-top: 0.3rem;">
          ✓ <strong>Correct Logic:</strong> Option ${m.correct_option} — ${m.concept}
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

  container.innerHTML = "<p style='text-align: center; color: var(--text-muted);'>Fetching candidate record...</p>";

  try {
    const res = await fetch(`/api/parent/report?phone=${encodeURIComponent(phone)}`);
    const data = await res.json();
    if (data.status === "success" && data.report) {
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
      body: JSON.stringify({ phone: currentUser ? currentUser.phone : "2348012345678", message: msg })
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
    document.getElementById("modalPlanTitle").textContent = "Activate " + data.plan_name;
    document.getElementById("modalAmountDisplay").textContent = "₦" + Number(data.amount_ngn).toLocaleString();
    document.getElementById("modalAccountNumber").textContent = data.virtual_account.account_number;
    modal.classList.add("active");
  }
}

async function simulatePaymentSuccess() {
  const res = await fetch("/api/payments/verify", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ reference: "PMS_" + Date.now(), plan_id: activePlan || "monthly" })
  });
  const data = await res.json();
  alert(data.message);
  closeModal("paymentModal");
  checkAuth();
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
    alert(data.message);
    document.getElementById("voucherInput").value = "";
    checkAuth();
  } else {
    alert(data.error);
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
      history: sessionHistory
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

function closeModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.remove("active");
}

// ----------------- COUNTDOWN TIMER -----------------
function startExamCountdown() {
  const targetDate = new Date();
  targetDate.setDate(targetDate.getDate() + 54);

  setInterval(() => {
    const now = new Date().getTime();
    const distance = targetDate - now;

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
