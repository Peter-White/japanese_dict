from django.test import TestCase
from kanji.models import KanjiBody, KanjiComprised, KanjiDefinition, KanjiPronunciation
from app.scripts.reference import jref
from kanji.scripts.prop_scripts import order_manage
from app.scripts.tests import mock_db

# Create your tests here.
class KanjiBodyTest(TestCase):
    def setUp(self):
        KanjiBody.objects.create(body = "日", strokes = 4)
        KanjiBody.objects.create(body = "本", strokes = 5)
        KanjiBody.objects.create(body = "一", strokes = 1)
        KanjiBody.objects.create(body = "木", strokes = 4)

        KanjiComprised.objects.create(kanji=KanjiBody.objects.get(body="本"), order=1, body=KanjiBody.objects.get(body="一"))
        KanjiComprised.objects.create(kanji=KanjiBody.objects.get(body="本"), order=2, body=KanjiBody.objects.get(body="木"))

        KanjiDefinition.objects.create(kanji=KanjiBody.objects.get(body="一"), order=1, type="N", lang="EN", body="One")
        KanjiDefinition.objects.create(kanji=KanjiBody.objects.get(body="本"), order=1, type="N", lang="EN", body="Book")
        KanjiDefinition.objects.create(kanji=KanjiBody.objects.get(body="木"), order=1, type="N", lang="EN", body="Tree")
        KanjiDefinition.objects.create(kanji=KanjiBody.objects.get(body="日"), order=1, type="N", lang="EN", body="Tree")
        

    def test_kanji_body(self):
        ni = KanjiBody.objects.get(body = "日")

        self.assertEqual(ni.get_body(), "日")

    def test_kanji_comprised(self):
        hon_test = KanjiComprised.objects.all().filter(kanji=2)

        body = hon_test[0].get_body()
        kanji = hon_test[0].get_kanji()

        test = body.get_body() == "一" and kanji.get_body() == "本"

        self.assertTrue(test)
