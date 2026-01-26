from django.db import models

class Particle(models.Model):
    body = models.CharField(max_length=20, unique=True)
    romaji = models.CharField(max_length=10, unique=True)
    use = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'particles'

    def __str__(self):
        return self.gana_ref + " (" + self.romaji + ")"

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
    def get_use(self):
        return self.use
    
    @property
    def get_description(self):
        return self.description