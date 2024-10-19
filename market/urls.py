from rest_framework import routers
from .views import UtilisateurViewSet, CategorieViewSet, ProduitViewSet, LignesCommandeViewSet

router = routers.DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'produits', ProduitViewSet)
router.register(r'commandes', LignesCommandeViewSet, basename='commandes')
