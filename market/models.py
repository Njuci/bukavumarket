from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# Modèle Utilisateur personnalisé
class Utilisateur(AbstractUser):
    USER_TYPES = [
        ('acheteur', 'Acheteur'),
        ('vendeur', 'Vendeur'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_type', 'email']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_type})"


# Modèle Categorie
class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.nom


# Modèle Produit
class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    vendeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='produits')
    date_ajout = models.DateTimeField(default=timezone.now)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    couleur = models.CharField(max_length=50, null=True)
    taille = models.CharField(max_length=50, null=True)

    def clean(self):
        if self.prix <= 0:
            raise ValidationError("Le prix doit être supérieur à zéro.")
        if self.vendeur.user_type != 'vendeur':
            raise ValidationError("Le vendeur doit avoir un rôle de vendeur.")

    def __str__(self):
        return self.nom


# Modèle Adresse
class Adresse(models.Model):
    adresse = models.TextField()
    ville = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    pays = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.adresse}, {self.ville}, {self.pays}"


# Modèle Commande (ligne de commande) sans acheteur
class Commande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='commandes')
    quantite = models.IntegerField()
    date_commande = models.DateTimeField(default=timezone.now)

    def clean(self):
        if self.quantite <= 0:
            raise ValidationError("La quantité doit être supérieure à zéro.")

    def __str__(self):
        return f"{self.quantite} de {self.produit.nom}"


# Modèle LignesCommande (commande complète) avec acheteur
class LignesCommande(models.Model):
    acheteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='commandes')
    lignes_commande = models.ManyToManyField(Commande, related_name='lignes_commande')
    date_commande = models.DateTimeField(default=timezone.now)
    statut_ligne = [
        ('en_attente', 'En attente'),
        ('valide', 'Validée'),
        ('annulee', 'Annulée'),
    ]
    statut = models.CharField(max_length=50, default='en_attente', choices=statut_ligne)

    def total(self):
        return sum(ligne.produit.prix * ligne.quantite for ligne in self.lignes_commande.all())

    def __str__(self):
        return f"Commande de {self.acheteur} du {self.date_commande}"

    def clean(self):
        if self.lignes_commande.count() == 0:
            raise ValidationError("La commande doit contenir au moins une ligne de commande.")
        if self.acheteur.user_type != 'acheteur':
            raise ValidationError("L'acheteur doit avoir un rôle d'acheteur.")
        