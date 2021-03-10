from django.conf.urls import url
from django.urls import include
from lamp import views_lamp
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'api/lamps', views_lamp.LampListAPI,basename='lamp')
router.register('api/cat', views_lamp.CatViewSet,basename='cat')

urlpatterns=[
    url(r'',  include(router.urls)     )

]