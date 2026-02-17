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

    def get_id(self):
        return self.pk

    @property
    def get_body(self):
        return self.body
    
    @body.setter
    def set_body(self, body):
        self.body = body

    @property
    def get_strokes(self):
        return self.strokes
    
    @strokes.setter
    def set_strokes(self, strokes):
        self.strokes = strokes
    
    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["cat"] = "kanji"
        obj["body"] = self.body
        obj["strokes"] = self.strokes
        obj["defs"] = []
        obj["prons"] = []
        obj["com"] = []
        return obj

class KanjiDefinition(models.Model):
    kanji = models.ForeignKey(KanjiBody, verbose_name=("Definition"), on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=1, choices=DEFINITION_TYPES)
    lang = models.CharField(max_length=2, choices=DEFINITION_LANGS)
    body = models.TextField()

    class Meta:
        db_table = 'kanji_definitions'

    @property
    def get_id(self):
        return self.pk
    
    @property
    def get_kanji(self):
        return self.kanji
    
    @property
    def get_lang(self):
        return self.lang
    
    @lang.setter
    def set_lang(self, lang):
        self.lang = lang
    
    @property
    def get_body(self):
        return self.body
    
    @body.setter
    def set_body(self, body):
        self.body = body
    
    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["kanji"] = self.kanji
        obj["lang"] = self.lang
        obj["body"] = self.body
        return obj

class KanjiPronunciation(models.Model):
    kanji = models.ForeignKey(KanjiBody, verbose_name=("Pronunciation"), on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=1, choices=PRONUNCIATION_TYPES)
    body = models.TextField()

    class Meta:
        db_table = 'kanji_pronounciations'

    @property
    def get_id(self):
        return self.pk
    
    @property
    def get_kanji(self):
        return self.kanji
    
    @property
    def get_type(self):
        return self.type

    @type.setter
    def set_type(self, type):
        self.type = type
    
    @property
    def get_body(self):
        return self.body
    
    @body.setter
    def set_body(self, body):
        self.body = body
    
    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["kanji"] = self.kanji
        obj["type"] = self.type
        obj["body"] = self.body
        return obj

class KanjiComprised(models.Model):
    kanji = models.ForeignKey(KanjiBody, related_name="Child", on_delete=models.CASCADE, null=True)
    body = models.ForeignKey(KanjiBody, related_name="Parent", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'kanji_comprised'


    @property
    def get_id(self):
        return self.pk
    
    @property
    def get_kanji(self):
        return self.kanji
    
    @property
    def get_body(self):
        return self.body

    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["kanji"] = self.kanji
        obj["body"] = self.body
        return obj