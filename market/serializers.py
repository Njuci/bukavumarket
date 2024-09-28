from rest_framework import serializers 
from .models import Utilisateur,Boutique,Categorie,Produit,Commande,CommandeProduit,Livraison,Payement
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class BoutiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boutique
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

class CommandeProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandeProduit
        fields = '__all__'

class LivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livraison
        fields = '__all__'
        
class PayementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payement
        fields = '__all__'

        