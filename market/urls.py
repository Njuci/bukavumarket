from rest_framework import routers
from .views import (UtilisateurViewSet, CategorieViewSet, ProduitViewSet, LignesCommandeViewSet, EmailConfirmationViewSet)

router = routers.DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'produits', ProduitViewSet)
router.register(r'commandes', LignesCommandeViewSet, basename='commandes')
router.register(r'email-confirmation', EmailConfirmationViewSet, basename='email-confirmation')  # Correction ici

urlpatterns = router.urls  # Utilisez le routeur pour générer les URL
