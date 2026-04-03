from django.test import TestCase
from kanji.models import KanjiBody, KanjiComprised, KanjiDefinition, KanjiPronunciation
from app.scripts.reference import jref

# Create your tests here.
class KanjiBodyTest(TestCase):
    def setUp(self):
        KanjiBody.objects.create(body = "日", strokes = 4)
        KanjiBody.objects.create(body = "本", strokes = 5)

    def test_kanji_body(self):
        ni = KanjiBody.objects.get(body = "日")

        self.assertEqual(ni.get_body(), "日")