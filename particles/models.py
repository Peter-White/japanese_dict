from django.db import models

class Particle(models.Model):
    body = models.CharField(max_length=20, unique=True)
    romaji = models.CharField(max_length=10, unique=True)
    use = models.CharField(max_length=50)
    description = models.CharField()

    class Meta:
        db_table = 'particles'

    def __str__(self):
        return self.gana_ref + " (" + self.romaji + ")"
