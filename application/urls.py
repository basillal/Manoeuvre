from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),   
    path('itmanager', views.itmanager, name='itmanager'),
    path('registration/<str:event_name>', views.registration, name='registration'),

 
]











