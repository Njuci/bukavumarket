from django.urls import path, include
from rest_framework import routers
from .views import UtilisateurViewSet,BoutiqueViewSet,CategorieViewSet,ProduitViewSet,CommandeViewSet,CommandeProduitViewSet,LivraisonViewSet,PayementViewSet


router = routers.DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'boutiques', BoutiqueViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'produits', ProduitViewSet)
router.register(r'commandes', CommandeViewSet)
router.register(r'commandeproduits', CommandeProduitViewSet)
router.register(r'livraisons', LivraisonViewSet)
router.register(r'payements', PayementViewSet)
