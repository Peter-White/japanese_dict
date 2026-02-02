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
    body = models.CharField(max_length=1, unique=True)
    strokes = models.IntegerField()

    class Meta:
        db_table = 'kanji_bodies'

    @property
    def get_id(self):
        return self.pk
    
    @property
    def get_body(self):
        return self.body
    
    @property
    def get_strokes(self):
        return self.strokes

class KanjiDefinition(models.Model):
    body = models.ForeignKey(KanjiBody, verbose_name=("Definition"), on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=1, choices=DEFINITION_TYPES)
    lang = models.CharField(max_length=2, choices=DEFINITION_LANGS)
    definition = models.TextField()

    class Meta:
        db_table = 'kanji_definitions'

    @property
    def get_id(self):
        return self.pk
    
    @property
    def get_body(self):
        return self.body
    
    @property
    def get_lang(self):
        return self.lang
    
    @property
    def get_description(self):
        return self.definition

class KanjiPronunciation(models.Model):
    body = models.ForeignKey(KanjiBody, verbose_name=("Pronunciation"), on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=1, choices=PRONUNCIATION_TYPES)
    pronunciation = models.TextField()

    class Meta:
        db_table = 'kanji_pronounciations'

    @property
    def get_id(self):
        return self.pk
    
    @property
    def get_body(self):
        return self.body
    
    @property
    def get_type(self):
        return self.type
    
    @property
    def get_pronunciation(self):
        return self.pronunciation

class KanjiComprised(models.Model):
    body = models.ForeignKey(KanjiBody, related_name="Child", on_delete=models.CASCADE, null=True)
    comprised = models.ForeignKey(KanjiBody, related_name="Parent", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'kanji_comprised'


    @property
    def get_id(self):
        return self.pk
    
    @property
    def get_body(self):
        return self.body
    
    @property
    def get_comprised(self):
        return self.comprised

