from django.test import TestCase
from kanji.models import KanjiBody, KanjiComprised, KanjiDefinition, KanjiPronunciation
from app.scripts.reference import jref
from kanji.scripts.prop_scripts import order_manage
from app.scripts.tests import mock_db

# Create your tests here.
class KanjiBodyTest(TestCase):
    def setUp(self):
        mock_db.populate_gana()
        mock_db.populate_kana()
        KanjiBody.objects.create(body = "日", strokes = 4)
        KanjiBody.objects.create(body = "本", strokes = 5)
        KanjiBody.objects.create(body = "一", strokes = 1)
        KanjiBody.objects.create(body = "木", strokes = 4)

        KanjiComprised.objects.create(kanji=KanjiBody.objects.get(body="本"), order=1, body=KanjiBody.objects.get(body="一"))
        KanjiComprised.objects.create(kanji=KanjiBody.objects.get(body="本"), order=2, body=KanjiBody.objects.get(body="木"))
        
    def test_kanji_body(self):
        ni = KanjiBody.objects.get(body = "日")

        self.assertEqual(ni.get_body(), "日")

    def test_kanji_comprised(self):
        hon_test = KanjiComprised.objects.all().filter(kanji=2)

        body = hon_test[0].get_body()
        kanji = hon_test[0].get_kanji()

        test = body.get_body() == "一" and kanji.get_body() == "本"

        self.assertTrue(test)

    def test_kanji_def(self):
        KanjiDefinition.objects.create(kanji=KanjiBody.objects.get(body="一"), order=1, type="N", lang="EN", body="One")
        KanjiDefinition.objects.create(kanji=KanjiBody.objects.get(body="一"), order=2, type="N", lang="EN", body="Beginning; start")
        KanjiDefinition.objects.create(kanji=KanjiBody.objects.get(body="一"), order=3, type="N", lang="EN", body="Ace (cards)")

        hon = KanjiBody.objects.get(body="一")

        defs = KanjiDefinition.objects.all().filter(kanji=hon.get_id())

        self.assertEqual(len(defs), 3)

    def test_kanji_pron(self):
        kanji=KanjiBody.objects.get(body="一")
        KanjiPronunciation.objects.create(kanji=kanji, order=1, type="O", body="{CAT:katakana|ID:2}{CAT:katakana|ID:48}")

        pron = KanjiPronunciation.objects.get(kanji=kanji, order=1)

        ref = jref(pron.get_body())

        self.assertTrue(ref[0]["body"] + ref[1]["body"], "ichi")

    def test_kanji_ref(self):
        ni = KanjiBody.objects.get(body = "日")

        KanjiPronunciation.objects.create(kanji=ni, order=1, type="O", body="{CAT:katakana|ID:68}")
        kan_ref = jref("{CAT:kanji|ID:1|PRON:1}")

        self.assertEqual(kan_ref["body"], "日")
        self.assertEqual(kan_ref["prons"][0]["body"], "ニ")

