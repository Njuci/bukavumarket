from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from datetime import timedelta

# Création des modèles pour l'application Pango
class Utilisateur(AbstractUser):
    USER_TYPES = [
        ('acheteur', 'Acheteur'),
        ('vendeur', 'Vendeur'),
    ]
    # Champs supplémentaires pour les utilisateurs
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    USERNAME_FIELD = 'username'  # Champ pour l'authentification
    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_type', 'password', 'email']  # Champs obligatoires pour la création d'un utilisateur il y a des champs par défaut herité de la classe AbstractUser
    groups = models.ManyToManyField(Group, related_name='myuser_set', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='utilisateur_set', blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.user_type}"

class Boutique(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    proprietaire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='boutiques')
    date_creation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nom

    def clean(self):
        if self.proprietaire.user_type != 'vendeur':
            raise ValidationError("Seuls les utilisateurs de type 'vendeur' peuvent avoir une boutique.")

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    boutique = models.ForeignKey(Boutique, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    date_ajout = models.DateTimeField(default=timezone.now)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.PositiveIntegerField()
    couleur = models.CharField(max_length=50,null=True)
    taille = models.CharField(max_length=50,null=True)


    def __str__(self):
        return self.nom
    
class Commande(models.Model):
    STATUTS_COMMANDE = [
            ('en_attente', 'En attente'),
            ('livree', 'Livrée'),

        ]
    acheteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='commandes')
    produits = models.ManyToManyField(Produit, through='CommandeProduit')
    date_commande = models.DateTimeField(default=timezone.now)
    statut = models.CharField(max_length=10, choices=STATUTS_COMMANDE, default='en_attente')

    def __str__(self):
        return f"Commande {self.id} par {self.acheteur.username}"

class CommandeProduit(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom} pour la commande {self.commande.id}"


    
class Livraison(models.Model):
    STATUTS_LIVRAISON = [
            ('en_cours', 'En cours'),
            ('livree', 'Livrée'),
        ]
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE, related_name='livraison')
    adresse_livraison = models.CharField(max_length=255)
    date_livraison = models.DateTimeField(default=timezone.now() + timedelta(days=7))
    statut = models.CharField(max_length=50, choices=STATUTS_LIVRAISON, default='en_attente')
    def __str__(self):
        return f"Livraison pour la commande {self.commande.id} à {self.adresse_livraison}"
    
    
class Payement(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE, related_name='payement')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    mode_payement = models.CharField(max_length=50)
    date_payement = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Payement de {self.montant} pour la commande {self.commande.id}"
    
    def clean(self):
        if self.montant <= 0:
            raise ValidationError("Le montant du payement doit être supérieur à zéro.")
        if self.commande.statut != 'en_attente':
            raise ValidationError("La commande doit être en attente pour être payée.")
        
