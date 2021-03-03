from rest_framework import serializers
from lamp.models import Lamp,Category

class LampSerializer(serializers.ModelSerializer):

    class Meta:
        model=Lamp
        fields=('id',
                'name',
                'published',
                'phone',
                'category',)

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=(
                'title',)