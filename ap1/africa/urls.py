from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('marrocos',views.marrocos, name='marrocos'),
    path('gana',views.gana, name='gana'),
    path('nigeria',views.nigeria, name='nigeria'),
]