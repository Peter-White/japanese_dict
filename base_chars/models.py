from django.db import models

class Hiragana(models.Model):
    body = models.CharField(max_length=3, unique=True)
    romaji = models.CharField(max_length=3)
    group_num = models.IntegerField()

    class Meta:
        db_table = 'hiragana'
        
    def __str__(self):
        return self.symbol + " (" + self.romaji + ")"
    
    @property
    def get_id(self):
        return self.pk
    
    @property
    def get_body(self):
        return self.body
    
    @property
    def get_romaji(self):
        return self.romaji

    @property
    def get_group_num(self):
        return self.group_num
    
class Katakana(models.Model):
    body = models.CharField(max_length=3, unique=True)
    romaji = models.CharField(max_length=3)
    group_num = models.IntegerField()

    class Meta:
        db_table = 'katakana'
        
    def __str__(self):
        return self.symbol + " (" + self.romaji + ")"
    
    @property
    def get_id(self):
        return self.pk

    @property
    def get_body(self):
        return self.body
    
    @property
    def get_romaji(self):
        return self.romaji

    @property
    def get_group_num(self):
        return self.group_num