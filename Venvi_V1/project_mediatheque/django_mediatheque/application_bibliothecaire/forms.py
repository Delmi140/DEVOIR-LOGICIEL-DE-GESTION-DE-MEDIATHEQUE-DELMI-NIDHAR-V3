from django import forms

class Creationmembre(forms.Form):
    nom = forms.CharField(required=False)
    prenom = forms.CharField(required=False)
    Emprunt = forms.CharField(required=False)


class Updatemembre(forms.Form):
    nom = forms.CharField(required=False)
    prenom = forms.CharField(required=False)
    Emprunt = forms.CharField(required=False)

class Creationlivre(forms.Form):
    name = forms.CharField(required=False)
    auteur = forms.CharField(required=False)
    disponible = forms.CharField(required=False)
    emprunteur = forms.CharField(required=False)
    dateEmprunt = forms.CharField(required=False)

class Updatelivre(forms.Form):
    name = forms.CharField(required=False)
    auteur = forms.CharField(required=False)
    disponible = forms.CharField(required=False)
    emprunteur = forms.CharField(required=False)
    dateEmprunt = forms.CharField(required=False)

class Creationcd(forms.Form):
    name = forms.CharField(required=False)
    auteur = forms.CharField(required=False)
    disponible = forms.CharField(required=False)
    emprunteur = forms.CharField(required=False)
    dateEmprunt = forms.CharField(required=False)

class Updatecd(forms.Form):
    name = forms.CharField(required=False)
    auteur = forms.CharField(required=False)
    disponible = forms.CharField(required=False)
    emprunteur = forms.CharField(required=False)
    dateEmprunt = forms.CharField(required=False)


class Creationdvd(forms.Form):
    name = forms.CharField(required=False)
    auteur = forms.CharField(required=False)
    disponible = forms.CharField(required=False)
    emprunteur = forms.CharField(required=False)
    dateEmprunt = forms.CharField(required=False)


class Updatedvd(forms.Form):
    name = forms.CharField(required=False)
    auteur = forms.CharField(required=False)
    disponible = forms.CharField(required=False)
    emprunteur = forms.CharField(required=False)
    dateEmprunt = forms.CharField(required=False)

class Creationjdp(forms.Form):
    name = forms.CharField(required=False)
    createur = forms.CharField(required=False)


class Updatejdp(forms.Form):
    name = forms.CharField(required=False)
    createur = forms.CharField(required=False)