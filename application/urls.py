from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="")
]











# from django.urls import path, re_path
# from . import views
# urlpatterns=[
#    path('',views.index,name='index'),
#    path('registration',views.registration,name='registration'),
#    path('login',views.loginPage,name='login'),
#    path('logout',views.logoutUser,name='logout'),
#    path('advertisement',views.advertisement,name='advertisement'),
#    path('delete_advertisement/<int:id>',views.delete_advertisement,name='delete_advertisement'),
#    path('update_advertisement/<int:id>',views.update_advertisement,name='update_advertisement'), 
#    path('student_registration',views.student_registration,name='student_registration'), 
 


# ]