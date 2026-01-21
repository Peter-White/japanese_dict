from django.test import TestCase
import json
from base_chars.models import Katakana, Hiragana

# Create your tests here.
class HiraganaKatakanaTestCase(TestCase):
    def setUp(self):
        gana_path = "base_chars/init_data/gana_data.json"
        kana_path = "base_chars/init_data/kana_data.json"

        with open(gana_path, 'r+') as json_file:
            dict_formatted_data = json.load(json_file)

            for obj in dict_formatted_data:
                Hiragana.objects.create(body=obj["fields"]["body"], 
                                        romaji=obj["fields"]["romaji"],
                                        group_num=obj["fields"]["group_num"])
            
        with open(kana_path, 'r+') as json_file:
            dict_formatted_data = json.load(json_file)

            for obj in dict_formatted_data:
                Katakana.objects.create(body=obj["fields"]["body"], 
                                        romaji=obj["fields"]["romaji"],
                                        group_num=obj["fields"]["group_num"])

    def test_gana_populated(self):
        ganaList = Hiragana.objects.all()
        self.assertEqual(len(ganaList), 207)

    def test_kana_populated(self):
        kanaList = Katakana.objects.all()
        self.assertEqual(len(kanaList), 454)

    def test_grab_gana(self):
        gana = Hiragana.objects.get(id=1)
        self.assertEqual(gana.get_body, "あ")
    
    def test_group_num(self):
        kanaList = Hiragana.objects.all().filter(group_num=1)
        self.assertEqual(len(kanaList), 5)

    def test_spell_mario_kana(self):
        ma = Katakana.objects.get(body="マ")
        ri = Katakana.objects.get(body="リ")
        o = Katakana.objects.get(body="オ")

        name = ""
        name += ma.get_romaji
        name += ri.get_romaji
        name += o.get_romaji

        self.assertEqual(name, "mario")