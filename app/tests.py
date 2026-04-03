from django.test import TestCase
from scripts.reference import jref

# Create your tests here.
class AppTest(TestCase):
    def test(self):
        self.assertTrue(True)

class JrefTest(TestCase):
    def ref_string_to_jp_test(self):
        aRef = jref("{h1}")

        self.assertEqual(aRef[0]["body"], "あ")
