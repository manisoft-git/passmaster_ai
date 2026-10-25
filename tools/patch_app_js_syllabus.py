import re

with open("static/js/app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update practiceCurrentTopicQuestions to use cbt_drill_topic
target_1 = """async function practiceCurrentTopicQuestions() {
  if (!activeLessonData) return;
  const subj = activeLessonData.subject;
  const topic = activeLessonData.topic;"""

replacement_1 = """async function practiceCurrentTopicQuestions() {
  if (!activeLessonData) return;
  const subj = activeLessonData.subject;
  const topic = activeLessonData.cbt_drill_topic || activeLessonData.topic;"""

# 2. Enhance renderSyllabus to display rich subtopics and a direct Masterclass link
target_2 = """function renderSyllabus(syllabus) {
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
}"""

replacement_2 = """function renderSyllabus(syllabus) {
  const container = document.getElementById("syllabusGrid");
  if (!container) return;
  container.innerHTML = "";

  Object.entries(syllabus).forEach(([subject, details]) => {
    const card = document.createElement("div");
    card.style.background = "var(--bg-card)";
    card.style.padding = "1rem";
    card.style.borderRadius = "var(--radius-sm)";
    card.style.border = "1px solid var(--border-subtle)";

    const topicsHtml = details.topics.map((t, idx) => {
      const subtopicsPreview = (t.subtopics || []).slice(0, 3).join(", ");
      const hasMore = (t.subtopics || []).length > 3 ? "..." : "";
      return `
        <div style="margin-top: 0.6rem; padding-top: 0.5rem; border-top: 1px solid rgba(148, 163, 184, 0.1);">
          <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.82rem; margin-bottom: 0.2rem;">
            <strong style="color: #f8fafc;">${t.name}</strong>
            <span style="color: var(--accent-cyan); font-weight: 700; font-size: 0.76rem; background: rgba(6, 182, 212, 0.12); padding: 0.1rem 0.4rem; border-radius: 4px;">${t.weight_pct}% weight</span>
          </div>
          <div style="font-size: 0.73rem; color: var(--text-dim); margin-bottom: 0.35rem; line-height: 1.3;">
            🎯 <em>${subtopicsPreview}${hasMore}</em>
          </div>
          <div style="display: flex; gap: 0.4rem;">
            <button class="btn-pill" style="font-size: 0.7rem; padding: 0.2rem 0.5rem; color: #38bdf8; background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.25);" onclick="viewLessonVideoDirect('${subject.replace(/'/g, "\\\\'")}', '${t.name.replace(/'/g, "\\\\'")}', ${idx > 0 && !isSubscribedUser()})">
              🎬 Watch Masterclass
            </button>
            <button class="btn-pill" style="font-size: 0.7rem; padding: 0.2rem 0.5rem; color: #a7f3d0; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.25);" onclick="drillLeakTopic('${subject.replace(/'/g, "\\\\'")}', '${t.name.replace(/'/g, "\\\\'")}')">
              ⚡ Drill Qs
            </button>
          </div>
        </div>
      `;
    }).join("");

    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
        <h4 style="font-size: 1.02rem; font-weight: 800; color: #ffffff; margin: 0;">${subject}</h4>
        <span class="status-badge" style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; font-size: 0.7rem;">${details.topics.length} Topics</span>
      </div>
      <div style="font-size: 0.72rem; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem;">${details.weight_in_jamb} Questions in Official JAMB UTME</div>
      ${topicsHtml}
    `;
    container.appendChild(card);
  });
}

function isSubscribedUser() {
  return typeof currentUser !== "undefined" && currentUser && currentUser.is_subscribed;
}"""

content = content.replace("\r\n", "\n")
target_1 = target_1.replace("\r\n", "\n")
replacement_1 = replacement_1.replace("\r\n", "\n")
target_2 = target_2.replace("\r\n", "\n")
replacement_2 = replacement_2.replace("\r\n", "\n")

if target_1 in content:
    content = content.replace(target_1, replacement_1, 1)
    print("Patched target_1 (practiceCurrentTopicQuestions)!")
else:
    print("target_1 not found!")

if target_2 in content:
    content = content.replace(target_2, replacement_2, 1)
    print("Patched target_2 (renderSyllabus)!")
else:
    print("target_2 not found!")

with open("static/js/app.js", "w", encoding="utf-8") as f:
    f.write(content)
print("Finished updating static/js/app.js!")
