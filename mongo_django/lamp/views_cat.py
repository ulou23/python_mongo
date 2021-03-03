from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from lamp.models import Category
from lamp.serializers import CatSerializer

from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def cat_list(req):
    if req.method=='GET':
        cat=Category.objects.all()
        title=req.GET.get('title',None)
        if title is not None:
            cat=cat.filter(title__icontains=title)
        cat_serial=CatSerializer(cat,many=True)
        return JsonResponse(cat_serial.data,safe=False)

    elif req.method=="POST":
        cat_data=JSONParser().parse(req)
        cat_serial=CatSerializer(data=cat_data)
        if cat_serial.is_valid():
            cat_serial.save()
            return JsonResponse(cat_serial.data,status=status.HTTP_201_CREATED)
        return JsonResponse(cat_serial.errors,status=status.HTTP_400_BAD_REQUEST)