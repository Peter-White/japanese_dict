from django.db import models

PRONUNCIATION_TYPES = [
    ('O', 'On\'yomi'),
    ('K', 'kun\'yomi'),
    ('N', 'Nanori')
]

DEFINITION_TYPES = [
    ('N', 'Noun'),
    ('A', 'Adjective'),
    ('V', 'Verb'),
    ('P', 'Pronoun'),
    ('G', 'Greeting'),
    ('P', 'Phrase')
]

DEFINITION_LANGS = [
    ("EN", "English")
]

class KanjiBody(models.Model):
    boby = models.CharField(max_length=1, unique=True)
    strokes = models.IntegerField()

    class Meta:
        db_table = 'kanji_bodies'

class KanjiDefinition(models.Model):
    body = models.ForeignKey(KanjiBody, verbose_name=("Definition"), on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=1, choices=DEFINITION_TYPES)
    lang = models.CharField(max_length=2, choices=DEFINITION_LANGS)
    definition = models.TextField()

    class Meta:
        db_table = 'kanji_definitions'

class KanjiPronunciation(models.Model):
    body = models.ForeignKey(KanjiBody, verbose_name=("Pronunciation"), on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=1, choices=PRONUNCIATION_TYPES)
    body = models.TextField()

    class Meta:
        db_table = 'kanji_pronounciations'

class KanjiComprised(models.Model):
    body = models.ForeignKey(KanjiBody, related_name="Child", on_delete=models.CASCADE, null=True)
    comprised = models.ForeignKey(KanjiBody, related_name="Parent", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'kanji_comprised'