# registration_app/admin.py
from django.contrib import admin
from .models import Applicant_Details , Participants , CustomUser , IT_manager_Details ,IT_Quiz_Details , Coding_Details ,Web_Designing_Details ,Hackathon_Details,Treasure_hunt_Details,Gaming_Details,Short_film_Details, Team_name_list

admin.site.register(Applicant_Details)
admin.site.register(Participants)
admin.site.register(Coding_Details)
admin.site.register(CustomUser)
admin.site.register(IT_Quiz_Details)
admin.site.register(Gaming_Details)
admin.site.register(Short_film_Details)
admin.site.register(Web_Designing_Details)
admin.site.register(Hackathon_Details)
admin.site.register(Treasure_hunt_Details)

class ItmanagerAdmin(admin.ModelAdmin):
    # readonly_fields = ('user_id','username')
    list_display = ('team_name','team_leader','event_name','team_no')
admin.site.register(IT_manager_Details, ItmanagerAdmin)  
admin.site.register(Team_name_list) 
    