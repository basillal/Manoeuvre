from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    # path('registration/', views.registrationpage_view, name='registrationpage_view'),
    # path('', views.registration_view, name='registration_view'),
    # path('success/', views.success_page, name='success_page')  #
    # path('event_registration/', views.event_registration, name='event_registration')
    # path('event_registration/', views.event_registration, name='event_registration'),
    path('itmanager', views.itmanager, name='itmanager'),

 
]











