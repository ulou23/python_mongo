from rest_framework import viewsets
from lamp.models import Lamp,Category
from lamp.serializers import LampSerializer,CatSerializer

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class LampListAPI(viewsets.ModelViewSet):
    serializer_class = LampSerializer
    queryset = Lamp.objects.all()

class CatViewSet(viewsets.ModelViewSet):
    serializer_class = CatSerializer
    queryset = Category.objects.all()


