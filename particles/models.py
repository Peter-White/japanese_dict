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

    def get_id(self):
        return self.id

    def get_romaji(self):
        return self.romaji

    def set_romaji(self, romaji):
        self.romaji = romaji

    def get_use(self):
        return self.use

    def set_use(self, use):
        self.use = use

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_body(self):
        return self.body
 
    def set_body(self, body):
        self.body = body
    
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