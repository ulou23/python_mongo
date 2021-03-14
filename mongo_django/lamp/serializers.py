from rest_framework import serializers
from lamp.models import Lamp,Category


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class LampSerializer(serializers.ModelSerializer):


    class Meta:
        model=Lamp
        fields=['id',
                'name',
                'published',
                'phone',
                'person',
                'categories']
        depth=1




