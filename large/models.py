from django.db import models

DEFINITION_LANGS = [
    ("EN", "English")
]

class LargeBody(models.Model):
    body = models.CharField(unique=True)

    class Meta:
        db_table = 'large_bodies'

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
        obj["cat"] = "large"
        obj["body"] = self.body
        return obj

class LargeTranslation(models.Model):
    large = models.ForeignKey(LargeBody, verbose_name=("Translation"), on_delete=models.CASCADE, null=True)
    order = models.IntegerField()
    lang = models.CharField(max_length=2, choices=DEFINITION_LANGS, default="EN")
    body = models.TextField()

    class Meta:
        db_table = 'large_translations'

    def get_id(self):
        return self.pk

    def get_body(self):
        return self.body
    
    def set_body(self, body):
        self.body = body

    def get_order(self):
        return self.order
    
    def set_order(self, order):
        self.order = order

    def get_large(self):
        return self.large
    
    def set_large(self, large):
        self.large = large

    def get_lang(self):
        return self.lang
    
    def set_lang(self, lang):
        self.lang = lang

    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["order"] = self.order
        obj["lang"] = self.lang
        obj["body"] = self.body
        return obj