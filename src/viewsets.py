from rest_framework import viewsets
from src.models import Menu
from src.serializers import MenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.all()

