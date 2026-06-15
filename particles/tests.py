from django.test import TestCase
from app.scripts.tests import mock_db
from particles.models import Particle
from base_chars.models import Hiragana
from app.scripts.reference import jref

class ParticleTestCase(TestCase):
    def setUp(self):
        mock_db.populate_particles()
        mock_db.populate_gana()

    def test_part_populated(self):
        partList = Particle.objects.all()
        self.assertEqual(len(partList), 15)

    def test_grab_part(self):
        part = Particle.objects.get(id=1)
        body = part.get_body()

        self.assertEqual(body, "{CAT:hiragana|ID:76}")

    def test_grab_part_ref(self):
        part = Particle.objects.get(id=1)
        ref = jref(part.get_body())
        part.set_body(ref[0])
        part = part.to_dict

        self.assertEqual(part["body"]["body"], "は")