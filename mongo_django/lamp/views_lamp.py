from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from lamp.models import Lamp
from lamp.serializers import LampSerializer

from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def lamp_list(req):
    if req.method=='GET':
        lamp=Lamp.objects.all()
        name=req.GET.get('name',None)
        if name is not None:
            lamp=lamp.filter(name__icontains=name)
        lamp_serial=LampSerializer(lamp,many=True)
        return JsonResponse(lamp_serial.data,safe=False)

    elif req.method=="POST":
        lamp_data=JSONParser().parse(req)
        lamp_serial=LampSerializer(data=lamp_data)
        if lamp_serial.is_valid():
            lamp_serial.save()
            return JsonResponse(lamp_serial.data,status=status.HTTP_201_CREATED)
        return JsonResponse(lamp_serial.errors,status=status.HTTP_400_BAD_REQUEST)

    elif req.method =='DELETE':
       all=Lamp.objects.all().delete()
       return JsonResponse({'mmessage': ' {} deleted'.format(all[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def lapm_detail(req,pk):
    pass