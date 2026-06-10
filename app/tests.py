from django.test import TestCase
from app.scripts.reference import jref
from app.scripts.tests import mock_db

class JrefTest(TestCase):
    def setUp(self):
        mock_db.populate_gana()

    def test_string_to_jp_test(self):
        aRef = jref("{CAT:hiragana|ID:1}")
        test = aRef[0]["body"]

        self.assertEqual(test, "あ")

    # def test_jp_num_seperation(self):
    #     word = jref("21{CAT:hiragana|ID:12}{CAT:hiragana|ID:70}")

    #     self.assertEqual(True)

    # def test_ref_failure_to_convert(self):
    #     aRef = jref("h1")

    #     self.assertEqual(aRef, None)