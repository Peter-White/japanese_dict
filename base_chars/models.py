from django.db import models

class Hiragana(models.Model):
    body = models.CharField(max_length=3, unique=True)
    romaji = models.CharField(max_length=3)
    group_num = models.IntegerField()

    class Meta:
        db_table = 'hiragana'
        
    def __str__(self):
        return self.symbol + " (" + self.romaji + ")"
    
class Katakana(models.Model):
    body = models.CharField(max_length=3, unique=True)
    romaji = models.CharField(max_length=3)
    group_num = models.IntegerField()

    class Meta:
        db_table = 'katakana'
        
    def __str__(self):
        return self.symbol + " (" + self.romaji + ")"