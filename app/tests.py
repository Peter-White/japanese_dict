from django.test import TestCase
from app.scripts.reference import jref

class JrefTest(TestCase):
    # def test_string_to_jp_test(self):
    #     aRef = jref("{CAT:'hiragana', ID:'1'}")

    #     self.assertEqual(aRef[0]["body"], "あ")

    def test_jp_num_seperation(self):
        word = jref("21{CAT:hiragana|ID:12}{CAT:hiragana|ID:70}")

        self.assertEqual(True)

    # def test_ref_failure_to_convert(self):
    #     aRef = jref("h1")

    #     self.assertEqual(aRef, None)