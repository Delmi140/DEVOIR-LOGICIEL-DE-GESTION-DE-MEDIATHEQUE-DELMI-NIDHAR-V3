from django.test import TestCase
from .models import Livre

class LivreTestCase(TestCase):
    def setUp(self):
        self.Livre = Livre.objects.create(name = 'Le malade imaginaire')


    def test_is_correct_instance(self):
        self.assertIsInstance(self.Livre, Livre)

    def test_exists(self):
        livre = Livre.objects.get(pk = 1)
        self.assertTrue(livre)