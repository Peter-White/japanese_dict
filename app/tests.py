from django.test import TestCase
from app.scripts.reference import jref

class JrefTest(TestCase):
    # def test_string_to_jp_test(self):
    #     aRef = jref("{h1}")

    #     self.assertEqual(aRef[0]["body"], "あ")

    # def test_jp_num_seperation(self):
    #     word = jref("21{h2}{h70}")

    #     self.assertEqual(True)

    # def test_ref_failure_to_convert(self):
    #     aRef = jref("h1")

    #     self.assertEqual(aRef, None)