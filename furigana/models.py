from django.db import models

class Hiragna(models.Model):
    symbol = models.CharField(max_length=3, unique=true)
    romaji = models.CharField(max_length=3)
    particle_rom = models.CharField(max_length=3)
    
class Katagana(models.Model):
    symbol = models.CharField(max_length=3, unique=true)
    romaji = models.CharField(max_length=3)