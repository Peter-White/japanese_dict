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
    def id(self):
        return self.pk
    
    @property
    def body(self):
        return self.body
    
    @body.setter
    def body(self, body):
        self.body = body
    
    @property
    def romaji(self):
        return self.romaji
    
    @romaji.setter
    def romaji(self, romaji):
        self.romaji = romaji
    
    @property
    def use(self):
        return self.use
    
    @use.setter
    def use(self, use):
        self.use = use
    
    @property
    def description(self):
        return self.description
    
    @property
    def description(self, description):
        self.description = description
    
    @property
    def to_dict(self):
        obj = {}
        obj["id"] = self.pk
        obj["cat"] = "particle"
        obj["body"] = self.body
        obj["rom"] = self.romaji
        obj["desc"] = self.description
        obj["use"] = self.use
        return obj