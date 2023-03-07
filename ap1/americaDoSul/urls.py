from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('brasil',views.brasil, name='brasil'),
    path('argentina',views.argentina, name='argentina')
]