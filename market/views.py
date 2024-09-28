from rest_framework import viewsets
from .models import Utilisateur,Boutique,Categorie,Produit,Commande,CommandeProduit,Livraison,Payement
from .serializers import UtilisateurSerializer,BoutiqueSerializer,CategorieSerializer,ProduitSerializer,CommandeSerializer,CommandeProduitSerializer,LivraisonSerializer,PayementSerializer
from .filtres import UtilisateurFilter,BoutiqueFilter,CategorieFilter,ProduitFilter,CommandeFilter,CommandeProduitFilter,LivraisonFilter,PayementFilter

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    filterset_class = UtilisateurFilter

class BoutiqueViewSet(viewsets.ModelViewSet):
    queryset = Boutique.objects.all()
    serializer_class = BoutiqueSerializer
    filterset_class = BoutiqueFilter

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    filterset_class = CategorieFilter

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    filterset_class = ProduitFilter

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    filterset_class = CommandeFilter

class CommandeProduitViewSet(viewsets.ModelViewSet):
    queryset = CommandeProduit.objects.all()
    serializer_class = CommandeProduitSerializer
    filterset_class = CommandeProduitFilter

class LivraisonViewSet(viewsets.ModelViewSet):
    queryset = Livraison.objects.all()
    serializer_class = LivraisonSerializer
    filterset_class = LivraisonFilter

class PayementViewSet(viewsets.ModelViewSet):
    queryset = Payement.objects.all()
    serializer_class = PayementSerializer
    filterset_class = PayementFilter
    
    