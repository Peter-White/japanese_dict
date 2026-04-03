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

    def get_body(self):
        return self.body
    
    def set_body(self, body):
        self.body = body

    def get_strokes(self):
        return self.strokes
    
    def set_strokes(self, strokes):
        self.strokes = strokes
    
    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["cat"] = "kanji"
        obj["body"] = self.body
        obj["strokes"] = self.strokes
        obj["defts"] = []
        obj["prons"] = []
        obj["com"] = []
        return obj

class KanjiDefinition(models.Model):
    kanji = models.ForeignKey(KanjiBody, verbose_name=("Definition"), on_delete=models.CASCADE, null=True)
    order = models.IntegerField()
    type = models.CharField(max_length=1, choices=DEFINITION_TYPES, default="N")
    lang = models.CharField(max_length=2, choices=DEFINITION_LANGS, default="EN")
    body = models.TextField()

    class Meta:
        db_table = 'kanji_definitions'

    def get_id(self):
        return self.pk
    
    def get_kanji(self):
        return self.kanji
    
    def get_order(self):
        return self.order
    
    def set_order(self, order):
        self.order = order
    
    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type
    
    def get_lang(self):
        return self.lang
    
    def set_lang(self, lang):
        self.lang = lang
    
    def get_body(self):
        return self.body
 
    def set_body(self, body):
        self.body = body
    
    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["order"] = self.order
        obj["lang"] = self.lang
        obj["type"] = self.type
        obj["body"] = self.body
        return obj

class KanjiPronunciation(models.Model):
    kanji = models.ForeignKey(KanjiBody, verbose_name=("Pronunciation"), on_delete=models.CASCADE, null=True)
    order = models.IntegerField()
    type = models.CharField(max_length=1, choices=PRONUNCIATION_TYPES, default="O")
    body = models.TextField()

    class Meta:
        db_table = 'kanji_pronounciations'

    def get_id(self):
        return self.pk
    
    def get_kanji(self):
        return self.kanji
    
    def get_order(self):
        return self.order
    
    def set_order(self, order):
        self.order = order
    
    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_body(self):
        return self.body

    def set_body(self, body):
        self.body = body
    
    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["order"] = self.order
        obj["type"] = self.type
        obj["body"] = self.body
        return obj

class KanjiComprised(models.Model):
    kanji = models.ForeignKey(KanjiBody, related_name="Child", on_delete=models.CASCADE, null=True)
    order = models.IntegerField()
    body = models.ForeignKey(KanjiBody, related_name="Parent", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'kanji_comprised'

    def get_id(self):
        return self.pk
    
    def get_order(self):
        return self.order
    
    def set_order(self, order):
        self.order = order
    
    def get_kanji(self):
        return self.kanji
    
    def get_body(self):
        return self.body
    
    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["order"] = self.order
        obj["com_id"] = self.body.get_id()
        obj["body"] = self.body.get_body()
        return obj