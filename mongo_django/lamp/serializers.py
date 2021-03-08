from rest_framework import serializers
from lamp.models import Lamp,Category


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'title',)

class LampSerializer(serializers.ModelSerializer):
    category=CatSerializer(read_only=True,required=False,many=True)

    class Meta:
        model=Lamp
        fields=('pk',
                'name',
                'published',
                'phone',
                'category',)




