from django.db import models

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

class WordBody(models.Model):
    body = models.CharField(max_length=1, unique=True)

    class Meta:
        db_table = 'word_bodies'

    def get_id(self):
        return self.pk

    def get_body(self):
        return self.body
    
    def set_body(self, body):
        self.body = body

    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["cat"] = "word"
        obj["body"] = self.body
        obj["defts"] = []
        obj["alts"] = []
        obj["syms"] = []
        obj["ants"] = []
        return obj

class WordDefinition(models.Model):
    word = models.ForeignKey(WordBody, verbose_name=("Definition"), on_delete=models.CASCADE, null=True)
    order = models.IntegerField()
    type = models.CharField(max_length=1, choices=DEFINITION_TYPES, default="N")
    lang = models.CharField(max_length=2, choices=DEFINITION_LANGS, default="EN")
    body = models.TextField()

    class Meta:
        db_table = 'word_definitions'

    def get_id(self):
        return self.pk

    def get_body(self):
        return self.body
    
    def set_body(self, body):
        self.body = body

    def get_word(self):
        return self.word
    
    def set_word(self, word):
        self.word = word

    def get_order(self):
        return self.order
    
    def set_order(self, order):
        self.order = order

    def get_lang(self):
        return self.lang
    
    def set_lang(self, lang):
        self.lang = lang

    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type

    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["order"] = self.order
        obj["lang"] = self.lang
        obj["type"] = self.type
        obj["body"] = self.body
        return obj

class WordSynonym(models.Model):
    word = models.ForeignKey(WordBody, related_name=("original_sym"), on_delete=models.CASCADE, null=True)
    alt = models.ForeignKey(WordBody, related_name=("alternative_sym"), on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'word_synonyms'

    def get_id(self):
        return self.pk
    
    def get_word(self):
        return self.word
    
    def get_alt(self):
        return self.alt
    
    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["word_id"] = self.word.get_id()
        obj["alt_id"] = self.alt.get_id()
        return obj

class WordAntonym(models.Model):
    word = models.ForeignKey(WordBody, related_name=("original_ant"), on_delete=models.CASCADE, null=True)
    alt = models.ForeignKey(WordBody, related_name=("alternative_ant"), on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'word_antonyms'

    def get_id(self):
        return self.pk
    
    def get_word(self):
        return self.word
    
    def get_alt(self):
        return self.alt
    
    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["word_id"] = self.word.get_id()
        obj["alt_id"] = self.alt.get_id()
        return obj