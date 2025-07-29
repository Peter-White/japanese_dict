from django.db import models

class Hiragana(models.Model):
    symbol = models.CharField(max_length=3, unique=True)
    romaji = models.CharField(max_length=3)
    
class Katakana(models.Model):
    symbol = models.CharField(max_length=3, unique=True)
    romaji = models.CharField(max_length=3)