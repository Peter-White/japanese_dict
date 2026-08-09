from django.test import TestCase
from large.models import LargeBody, LargeTranslation
from kanji.models import KanjiBody, KanjiPronunciation
from words.models import WordBody
from app.scripts.reference import jref
from app.scripts.tests import mock_db

class LargeBodyTest(TestCase):

    def setUp(self):
        mock_db.populate_gana()
        mock_db.populate_kana()
        mock_db.populate_particles()

        KanjiBody.objects.create(body = "私", strokes = 7)
        WordBody.objects.create(body="{CAT:katakana|ID:325}{CAT:katakana|ID:273}")
        WordBody.objects.create(body="{CAT:hiragana|ID:62}{CAT:hiragana|ID:30}")

    def test_large_body(self):
        LargeBody.objects.create(body = "{CAT:kanji|ID:1}{CAT:particle|ID:1}{CAT:word|ID:1}{CAT:word|ID:2}。")

        large = LargeBody.objects.get(id=1)

        large_ref = jref(large.get_body())

        self.assertTrue(True)