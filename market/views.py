from rest_framework import viewsets
from .models import Utilisateur,Categorie,Produit,Commande
from .serializers import *
from .filtres import *
class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    filterset_class = UtilisateurFilter


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


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
class LignesCommandeViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les commandes et les lignes de commande associées.
    """
    queryset = LignesCommande.objects.all()
    serializer_class = LignesCommandeSerializer

    def retrieve(self, request, pk=None):
        """
        Récupérer une commande spécifique si l'ID est fourni ou toutes les commandes.
        """
        ligne_commande = get_object_or_404(LignesCommande, pk=pk)
        serializer = LignesCommandeSerializer(ligne_commande)
        return Response(serializer.data)
    def create(self, validated_data):
        lignes_commande_data = validated_data.pop('lignes_commande')
        commande = Commande.objects.create(**validated_data)
        
        # Créer et assigner toutes les lignes de commande en une fois
        lignes_commande = [LignesCommande.objects.create(**ligne_data) for ligne_data in lignes_commande_data]
        commande.lignes_commande.set(lignes_commande)

        return commande

    def update(self, request, pk=None):
        """
        Mettre à jour une commande existante.
        """
        ligne_commande = get_object_or_404(LignesCommande, pk=pk)
        serializer = LignesCommandeSerializer(ligne_commande, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)