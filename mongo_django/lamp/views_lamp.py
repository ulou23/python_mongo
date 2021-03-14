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


# new

from rest_framework import generics
class CategoryList(generics.ListAPIView):
    serializer_class = CatSerializer
    queryset = Category.objects.all()

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer

class LampList(generics.ListCreateAPIView):
    queryset = Lamp.objects.all()
    serializer_class = LampSerializer

class LampDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lamp.objects.all()
    serializer_class = LampSerializer




