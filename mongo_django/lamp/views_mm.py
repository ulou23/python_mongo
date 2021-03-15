from rest_framework import viewsets  , generics     ,views
from lamp.models import Lamp,Category
from lamp.serializers import LampSerializer,CatSerializer

from rest_framework.response import Response

class LampView(viewsets.ModelViewSet):
    serializer_class = LampSerializer

    def get_queryset(self):
        lamp=Lamp.objects.all()
        return lamp

    def create(self, request, *args, **kwargs):
        data=request.data
        new_lamp=Lamp.objects.create(
            name=data["name"], phone=data["phone"], person=data["person"]
        )
        new_lamp.save()

        for cat in data["categories"]:
            cat_obj=Category.objects.get(title=cat["title"])
            new_lamp.categories.add(cat_obj)

        serializer=LampSerializer(new_lamp)
        return Response(serializer.data)

class CatView(viewsets.ModelViewSet):
    
    serializer_class = CatSerializer
    def get_queryset(self):
        cat=Category.objects.all()
        return cat

from django_filters.rest_framework import DjangoFilterBackend
import django_filters


class CatFilter(viewsets.ModelViewSet):
    queryset = Lamp.objects.all()

    def get_queryset(self):
        return self.queryset \
    .filter(category=self.kwargs.get('categories'))