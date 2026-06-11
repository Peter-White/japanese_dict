from django.test import TestCase
import json
from app.scripts.tests import mock_db
from base_chars.models import Katakana, Hiragana

# Create your tests here.
class HiraganaKatakanaTestCase(TestCase):
    def setUp(self):
        mock_db.populate_gana()
        mock_db.populate_kana()

    def test_gana_populated(self):
        ganaList = Hiragana.objects.all()
        self.assertEqual(len(ganaList), 207)

    def test_kana_populated(self):
        kanaList = Katakana.objects.all()
        self.assertEqual(len(kanaList), 454)

    def test_grab_gana(self):
        gana = Hiragana.objects.get(id=1)
        sym = gana.get_body()

        self.assertEqual(sym, "あ")
    
    def test_group_num(self):
        kanaList = Hiragana.objects.all().filter(group_num=1)
        self.assertEqual(len(kanaList), 5)

    def test_spell_mario_kana(self):
        ma = Katakana.objects.get(body="マ")
        ri = Katakana.objects.get(body="リ")
        o = Katakana.objects.get(body="オ")

        name = ""
        name += ma.get_romaji()
        name += ri.get_romaji()
        name += o.get_romaji()

        self.assertEqual(name, "mario")