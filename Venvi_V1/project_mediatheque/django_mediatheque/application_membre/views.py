from django.shortcuts import render
from application_bibliothecaire.models import Livre,Cd,Dvd,JeuxDePlateau

def listeMembreApp(request):
    livres = Livre.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()
    jdps = JeuxDePlateau.objects.all()

    return render(request, 'application/application_membre.html',
                  { 'livres': livres,  'cds': cds , 'dvds': dvds , 'jdps': jdps ,  } )