from django.test import TestCase
from kanji.models import KanjiBody, KanjiPronunciation
from words.models import WordBody
from app.scripts.reference import jref
from app.scripts.tests import mock_db

class WordBodyTest(TestCase):
    def setUp(self):
        mock_db.populate_gana()
        mock_db.populate_kana()
        mock_db.populate_particles()
        KanjiBody.objects.create(body = "日", strokes = 4)
        KanjiBody.objects.create(body = "本", strokes = 5)

    def test_word_ref_body(self):
        ni = KanjiBody.objects.get(body = "日")
        hon = KanjiBody.objects.get(body = "本")

        KanjiPronunciation.objects.create(kanji=ni, order=1, type="O", body="{CAT:katakana|ID:68}")
        KanjiPronunciation.objects.create(kanji=hon, order=2, type="O", body="{CAT:katakana|ID:84}{CAT:katakana|ID:135}")

        word = WordBody.objects.create(body="{CAT:kanji|ID:1|PRON:1}{CAT:kanji|ID:2|PRON:2}")

        word_bod = jref(word.get_body())

        kan_bod = ""
        pron_bod = ""
        rom = ""

        for kan_obj in word_bod:
            kan_bod += kan_obj["body"]

            for pron_obj in kan_obj['prons']:
                for bod_obj in pron_obj["body"]:
                    pron_bod += bod_obj['body']
                    rom += bod_obj['rom']

        self.assertEqual(kan_bod, "日本")
        self.assertEqual(pron_bod, 'ニホン')
        self.assertEqual(rom, "nihon")

    def test_word_pron(self):
        ni = KanjiBody.objects.get(body = "日")
        hon = KanjiBody.objects.get(body = "本")

        KanjiPronunciation.objects.create(kanji=ni, order=1, type="O", body="{CAT:katakana|ID:68}")
        KanjiPronunciation.objects.create(kanji=hon, order=1, type="O", body="{CAT:katakana|ID:84}{CAT:katakana|ID:135}")
        KanjiPronunciation.objects.create(kanji=hon, order=2, type="K", body="{CAT:hiragana|ID:114}{CAT:hiragana|ID:54}")

        word_ref = WordBody.objects.create(body="{CAT:kanji|ID:1|PRON:1}{CAT:kanji|ID:2|PRON:2|PRON:3}")

        word = jref(word_ref.get_body())

        word_bod = ""

        for kan in word:
            word_bod += kan['body']

        ni_prons = word[0]['prons']
        hon_prons = word[1]['prons']

        self.assertEqual(word_bod, "日本")

        self.assertEqual(ni_prons[0]['body'][0]['body'], 'ニ')

        hon_roms = []

        for pn in hon_prons:
            rom = ""

            for bd in pn['body']:
                rom += bd['rom']

            hon_roms.append(rom)

        self.assertEqual(hon_roms, ['hon', 'moto'])