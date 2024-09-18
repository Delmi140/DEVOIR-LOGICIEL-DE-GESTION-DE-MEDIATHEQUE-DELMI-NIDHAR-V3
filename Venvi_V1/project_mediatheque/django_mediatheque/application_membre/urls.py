from application_membre import views
from django.urls import path

urlpatterns = [

    path('', views.listeMembreApp),

]