from .models import Utilisateur,Boutique,Categorie,Produit,Commande,CommandeProduit,Livraison,Payement
import django_filters


class UtilisateurFilter(django_filters.FilterSet):
    class Meta:
        model = Utilisateur
        fields = ['username', 'first_name', 'last_name', 'user_type']

class BoutiqueFilter(django_filters.FilterSet):
    class Meta:
        model = Boutique
        fields = ['nom', 'description', 'proprietaire']

class CategorieFilter(django_filters.FilterSet):
    class Meta:
        model = Categorie
        fields = ['nom', 'description', 'boutique']

class ProduitFilter(django_filters.FilterSet):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'categorie', 'prix', 'quantite']

class CommandeFilter(django_filters.FilterSet):
    class Meta:
        model = Commande
        fields = ['acheteur', 'statut']

class CommandeProduitFilter(django_filters.FilterSet):
    class Meta:
        model = CommandeProduit
        fields = ['commande', 'produit', 'quantite']

class LivraisonFilter(django_filters.FilterSet):
    class Meta:
        model = Livraison
        fields = ['commande', 'adresse_livraison', 'statut']

class PayementFilter(django_filters.FilterSet):
    class Meta:
        model = Payement
        fields = ['commande', 'montant', 'mode_payement']
    