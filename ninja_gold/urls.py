from django.urls import path     
from . import views

urlpatterns = [
    path('', views.gold_home),
    path('process_gold', views.process_gold),
    path('reset', views.reset),
]