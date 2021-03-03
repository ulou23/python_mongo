from django.conf.urls import url
from lamp import views_lamp, views_cat

urlpatterns=[
    url(r'^api/lamps$', views_lamp.lamp_list)  ,
    url(r'^api/cat$', views_cat.cat_list)
]