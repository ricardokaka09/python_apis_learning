from rest_framework import routers
from src.viewsets import MenuViewSet
router = routers.SimpleRouter()
router.register(r'menu', MenuViewSet, basename='menu')