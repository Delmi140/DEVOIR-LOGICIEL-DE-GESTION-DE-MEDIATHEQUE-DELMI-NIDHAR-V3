from application_bibliothecaire import views

from django.urls import path

urlpatterns = [

    path('', views.connexion , name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('AppBibliothecaire/', views.listeMembre, name= 'AppBibliothecaire'),
    path('ajoutmembre/', views.ajoutmembre),
    path('updatemembre/<int:id>/', views.updatemembre),
    path('deletemembre/<int:id>/', views.deletemembre),
    path('ajoutlivre/', views.ajoutlivre),
    path('updatelivre/<int:id>/', views.updatelivre),
    path('deletelivre/<int:id>/', views.deletelivre),
    path('ajoutcd/', views.ajoutcd),
    path('updatecd/<int:id>/', views.updatecd),
    path('deletecd/<int:id>/', views.deletecd),
    path('ajoutdvd/', views.ajoutdvd),
    path('updatedvd/<int:id>/', views.updatedvd),
    path('deletedvd/<int:id>/', views.deletedvd),
    path('ajoutjdp/', views.ajoutjdp),
    path('updatejdp/<int:id>/', views.updatejdp),
    path('deletejdp/<int:id>/', views.deletejdp),




]
