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

    def test_string_to_jp_test2(self):
        aRef = jref("{CAT:hiragana|ID:76}")
        test = aRef[0]["body"]

        self.assertEqual(test, 'は')

    def test_jp_num_seperation(self):
        struct = jref("21{CAT:hiragana|ID:12}{CAT:hiragana|ID:70}")

        num = struct[0]
        h1 = struct[1]['body']
        h2 = struct[2]['body']

        self.assertEqual(num, "21")
        self.assertEqual(h1, 'け')
        self.assertEqual(h2, 'ぬ')

    # def test_ref_failure_to_convert(self):
    #     aRef = jref("h1")

    #     self.assertEqual(aRef, None)