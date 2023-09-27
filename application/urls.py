from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),    
    path('registration/<str:event_name>', views.registration, name='registration'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutUser,name='logout'),

 
]











