from django.contrib import admin
from .models import Utilisateur, Categorie, Produit, Commande, LignesCommande, Adresse

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(LignesCommande)
admin.site.register(Adresse)  # Ajout de l'adresse à l'interface d'administration