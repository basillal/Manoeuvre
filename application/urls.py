from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('event_registration/', views.event_registration, name='event_registration'),
    path('itmanager/', views.itmanager, name='itmanager')

]











