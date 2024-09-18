from django.db import models


class Membre(models.Model):
     nom = models.fields.CharField(max_length=150)
     prenom = models.fields.CharField(max_length=150)
     Emprunt = models.fields.CharField(max_length=150)


class Media(models.Model):


    class Meta:
        abstract = True


class Livre(Media):
    name = models.fields.CharField(max_length=150)
    auteur = models.fields.CharField(max_length=150)
    dateEmprunt = models.fields.CharField(max_length=150)
    disponible = models.fields.CharField(max_length=150)
    emprunteur = models.fields.CharField(max_length=150)


class Dvd(Media):
    name = models.fields.CharField(max_length=150)
    auteur = models.fields.CharField(max_length=150)
    dateEmprunt = models.fields.CharField(max_length=150)
    disponible = models.fields.CharField(max_length=150)
    emprunteur = models.fields.CharField(max_length=150)

class Cd(Media):
    name = models.fields.CharField(max_length=150)
    auteur = models.fields.CharField(max_length=150)
    dateEmprunt = models.fields.CharField(max_length=150)
    disponible = models.fields.CharField(max_length=150)
    emprunteur = models.fields.CharField(max_length=150)


class JeuxDePlateau(models.Model):
    name = models.fields.CharField(max_length=150)
    createur = models.fields.CharField(max_length=150)