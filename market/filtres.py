from .models import Utilisateur, Categorie, Produit, Commande, LignesCommande,Adresse
import django_filters


# Filtre pour le modèle Utilisateur
class UtilisateurFilter(django_filters.FilterSet):
    class Meta:
        model = Utilisateur
        fields = ['username', 'first_name', 'last_name', 'user_type']


# Filtre pour le modèle Categorie
class CategorieFilter(django_filters.FilterSet):
    class Meta:
        model = Categorie
        fields = ['nom', 'description']


# Filtre pour le modèle Produit
class ProduitFilter(django_filters.FilterSet):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'categorie', 'prix', 'couleur', 'taille']


# Filtre pour le modèle Commande (ligne de commande)
class CommandeFilter(django_filters.FilterSet):
    class Meta:
        model = Commande
        fields = ['produit', 'quantite', 'date_commande']


# Filtre pour le modèle LignesCommande (commande complète)
class LignesCommandeFilter(django_filters.FilterSet):
    class Meta:
        model = LignesCommande
        fields = ['acheteur', 'statut', 'date_commande']
class AdresseFilter(django_filters.FilterSet):
    class Meta:
        model=Adresse
        fields=['pays','adresse','ville']      

# Remarque : dans cette version, il n'y a pas de modèles explicites pour `Livraison` et `Payement`
# selon les informations fournies. Si tu as besoin de ces modèles, il faudra les ajouter et
# ajuster les filtres en conséquence.

