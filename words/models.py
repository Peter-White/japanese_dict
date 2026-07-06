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

# Create your models here.
class WordBody(models.Model):
    body = models.CharField(max_length=1, unique=True)

class WordDefinition(models.Model):
    word = models.ForeignKey(WordBody, verbose_name=("Definition"), on_delete=models.CASCADE, null=True)
    order = models.IntegerField()
    type = models.CharField(max_length=1, choices=DEFINITION_TYPES, default="N")
    lang = models.CharField(max_length=2, choices=DEFINITION_LANGS, default="EN")
    body = models.TextField()

class WordAltSpelling(models.Model):
    word = models.ForeignKey(WordBody, verbose_name=("Origianl"), on_delete=models.CASCADE, null=True)
    alt = models.ForeignKey(WordBody, verbose_name=("Alternative"), on_delete=models.CASCADE, null=True)

class WordSynonym(models.Model):
    word = models.ForeignKey(WordBody, verbose_name=("Origianl"), on_delete=models.CASCADE, null=True)
    alt = models.ForeignKey(WordBody, verbose_name=("Alternative"), on_delete=models.CASCADE, null=True)

class WordAntonym(models.Model):
    word = models.ForeignKey(WordBody, verbose_name=("Origianl"), on_delete=models.CASCADE, null=True)
    alt = models.ForeignKey(WordBody, verbose_name=("Alternative"), on_delete=models.CASCADE, null=True)