from rest_framework import serializers 
from .models import Utilisateur,Categorie,Produit,Commande,LignesCommande,Adresse
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

# Serializer pour une seule ligne de commande (Commande)
class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ['produit', 'quantite', 'date_commande']

    def validate_quantite(self, value):
        if value <= 0:
            raise serializers.ValidationError("La quantité doit être supérieure à zéro.")
        return value

# Serializer pour l'ensemble des commandes (LignesCommande)
class LignesCommandeSerializer(serializers.ModelSerializer):
    lignes_commande = CommandeSerializer(many=True)

    class Meta:
        model = LignesCommande
        fields = ['acheteur', 'lignes_commande', 'date_commande', 'statut']

    def create(self, validated_data):
        lignes_commande = validated_data.pop('lignes_commande')
        lignes_commande_instance = LignesCommande(**validated_data)
        lignes_commande_instance.clean()  # Validation ici
        lignes_commande_instance.save()
        lignes_commande_instance.lignes_commande.set(lignes_commande)
        return lignes_commande_instance
    def validate(self, data):
        if not data.get('lignes_commande'):
            raise serializers.ValidationError("Une commande doit contenir au moins une ligne de commande.")
        return data
        
class AdresseSerial(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields = '__all__' 
        
               