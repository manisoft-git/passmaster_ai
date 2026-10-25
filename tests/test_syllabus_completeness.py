import sys, os
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import unittest
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app, load_lessons_db

class TestSyllabusCompleteness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        with open("data/syllabus.json", "r", encoding="utf-8") as f:
            cls.syllabus = json.load(f)
        cls.lessons = load_lessons_db()

    def test_all_8_subjects_present_in_syllabus(self):
        expected_subjects = [
            "Use of English", "Mathematics", "Physics", "Chemistry",
            "Biology", "Economics", "Government", "Literature in English"
        ]
        for subj in expected_subjects:
            self.assertIn(subj, self.syllabus, f"Missing subject: {subj}")
            self.assertIn(subj, self.lessons, f"Missing subject in lessons: {subj}")

    def test_each_subject_has_6_topics_with_100_percent_weight(self):
        for subj, data in self.syllabus.items():
            topics = data.get("topics", [])
            self.assertEqual(len(topics), 6, f"Subject {subj} should have 6 topics, found {len(topics)}")
            total_weight = sum(t.get("weight_pct", 0) for t in topics)
            self.assertEqual(total_weight, 100, f"Subject {subj} weights should sum to 100%, got {total_weight}%")
            
            # Verify each topic has at least 4 subtopics and a description
            for t in topics:
                self.assertTrue(len(t.get("subtopics", [])) >= 4, f"{subj} -> {t['name']} has fewer than 4 subtopics")
                self.assertTrue(len(t.get("description", "")) > 20, f"{subj} -> {t['name']} missing rich description")

    def test_lessons_1_to_1_parity_with_syllabus(self):
        for subj, data in self.syllabus.items():
            syl_topic_names = [t["name"] for t in data["topics"]]
            les_topic_names = [l["topic"] for l in self.lessons.get(subj, [])]
            self.assertEqual(sorted(syl_topic_names), sorted(les_topic_names),
                             f"Topic mismatch in {subj}:\nSyllabus: {syl_topic_names}\nLessons: {les_topic_names}")

    def test_every_lesson_has_3_video_modules(self):
        total_modules = 0
        for subj, lesson_list in self.lessons.items():
            for les in lesson_list:
                vm = les.get("video_meta")
                self.assertIsNotNone(vm, f"Lesson {les['topic']} missing video_meta")
                modules = vm.get("modules", [])
                self.assertEqual(len(modules), 3, f"Lesson {les['topic']} should have 3 video modules")
                total_modules += len(modules)
                for mod in modules:
                    yt = mod.get("youtube_id", "")
                    self.assertTrue(yt and len(yt) >= 6 and "_xWp-zN85_Y" not in yt,
                                    f"Invalid YouTube ID '{yt}' in {subj} -> {les['topic']}")

        self.assertEqual(total_modules, 144, f"Expected 144 video modules, found {total_modules}")

    def test_all_48_topics_return_cbt_drill_questions(self):
        for subj, data in self.syllabus.items():
            for t in data["topics"]:
                top_name = t["name"]
                res = self.client.get(f"/api/questions?subject={subj}&topic={top_name}&limit=5")
                self.assertEqual(res.status_code, 200)
                count = res.json.get("count", 0)
                self.assertTrue(count >= 5, f"Drill for {subj} -> {top_name} returned only {count} questions")

if __name__ == "__main__":
    unittest.main()
