from rest_framework import serializers
from lamp.models import Lamp,Category


class LampSerializer(serializers.ModelSerializer):
    category=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),many=True)

    class Meta:
        model=Lamp
        fields=('id',
                'name',
                'published',
                'phone',
                'category',)

class CatSerializer(serializers.ModelSerializer):
    lamps = LampSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ( 'title', 'lamps')


