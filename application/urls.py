from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
<<<<<<< HEAD
    path('registration/', views.registrationpage_view, name='registrationpage_view'),
    path('', views.registration_view, name='registration_view'),
    path('success/', views.success_page, name='success_page')  # Create a success page view

=======
    path('event_registration/', views.event_registration, name='event_registration')
>>>>>>> registration
]











