from django.conf.urls import url
from django.urls import include,path
from lamp import views_lamp
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from django_filters.views import FilterView

from lamp.views_mm import LampView, CatView ,CatFilter

router=DefaultRouter()
router.register('mmlamps', LampView,basename='lamp')
router.register('mmcat', CatView ,basename='cat')


urlpatterns=[
    url('', include(router.urls))     ,
     
   # path('',  include(router.urls)     ) ,
    path('category/', views_lamp.CategoryList.as_view()),
    path('category/<int:pk>/',views_lamp.CategoryDetail.as_view()),
    path('lamps/<int:pk>/', views_lamp.LampDetail.as_view())  ,
    path('lamps/', views_lamp.LampList.as_view())

]

