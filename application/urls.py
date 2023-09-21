from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),   
    path('itmanager', views.itmanager, name='itmanager'),
    path('registration/<str:ITManager>', views.registration, name='registration'),

 
]











