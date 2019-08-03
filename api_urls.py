from django.urls import path,include
#from .import views
from rest_framework import viewsets
from cookbook import views
from rest_framework import routers



urlpatterns = [
    path('api/',views.ReceipeViewSet.as_view()),
    path('api/<int:pk>/',views.ReceipeViewSet.as_view()),
    #path('api/put/(?P<pk>[\w:|-]+)/',views.ReceipeViewSet.as_view()),
    #path('api/delete/(?P<pk>[\w:|-]+)/',views.ReceipeViewSet.as_view()),
    #path('cookbook',include(router.urls)),
]
