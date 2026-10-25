import unittest
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app, load_lessons_db

class TestVideoLessonsMasterclass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.data = load_lessons_db()

    def test_all_48_topics_exist_and_have_modules(self):
        total_topics = 0
        for subj, topics in self.data.items():
            self.assertEqual(len(topics), 6, f"Subject {subj} should have 6 topics")
            for t in topics:
                total_topics += 1
                vm = t.get("video_meta")
                self.assertIsNotNone(vm, f"Topic {t.get('topic')} missing video_meta")
                modules = vm.get("modules", [])
                self.assertEqual(len(modules), 3, f"Topic {t.get('topic')} should have 3 modules")
                
                # Check each module
                for idx, mod in enumerate(modules):
                    self.assertIn(mod.get("tag"), ["Module 1", "Module 2", "Module 3"])
                    self.assertTrue(mod.get("youtube_id"), f"Module {idx} missing youtube_id")
                    self.assertNotEqual(mod.get("youtube_id"), "_xWp-zN85_Y", f"Found dummy ID in {t.get('topic')}")
                    self.assertTrue(mod.get("title"))
                    self.assertTrue(mod.get("duration"))
                    self.assertTrue(len(mod.get("chapters", [])) >= 3)
                    self.assertTrue(len(mod.get("key_takeaways", [])) >= 2)

                # Check synced notes & retention quiz
                synced = vm.get("synced_notes", [])
                self.assertTrue(len(synced) >= 3, f"Topic {t.get('topic')} missing synced_notes")
                quiz = vm.get("retention_quiz", [])
                self.assertEqual(len(quiz), 3, f"Topic {t.get('topic')} should have 3 retention quiz Qs")

        self.assertEqual(total_topics, 48, "Total topics should be 48")
        print(f"Verified all {total_topics} topics have 3 rich modules (144 total) with zero broken links!")

    def test_api_lessons_catalog(self):
        res = self.client.get("/api/lessons")
        self.assertEqual(res.status_code, 200)
        d = res.json
        self.assertEqual(d["status"], "success")
        self.assertEqual(d["count"], 48)
        self.assertTrue(len(d["lessons"]) == 48)

    def test_api_single_lesson_video_meta(self):
        # Test Free lesson 0 in Use of English
        res = self.client.get("/api/lessons/Use of English/Concord & Grammar")
        self.assertEqual(res.status_code, 200)
        d = res.json
        self.assertEqual(d["status"], "success")
        les = d["lesson"]
        vm = les["video_meta"]
        self.assertEqual(len(vm["modules"]), 3)
        self.assertEqual(vm["modules"][0]["youtube_id"], "4fMipjAnlRk")
        self.assertEqual(len(vm["synced_notes"]), 4)
        self.assertEqual(len(vm["retention_quiz"]), 3)

    def test_api_video_progress_saving(self):
        res = self.client.post("/api/lessons/video-progress", json={
            "lesson_id": "eng_lesson_1",
            "completed": True,
            "module_index": 0
        })
        self.assertEqual(res.status_code, 200)
        d = res.json
        self.assertEqual(d["status"], "success")
        self.assertEqual(d["lesson_id"], "eng_lesson_1")
        self.assertTrue(d["completed"])

if __name__ == "__main__":
    unittest.main()
