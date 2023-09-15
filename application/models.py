from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

# Login details
class User():
    email = models.EmailField(
        primary_key=True
    )
    username = models.CharField(
        max_length= 100,
        null = False
    )
    password = models.CharField(
        max_length= 50,
        null = False
    )
    user_type = models.CharField(
        max_length=100,
        null=False
    )
    
    def get_full_name(self):
        return self.username
    
    def __str__(self):
        return self.email
    
# Applicant details loaded from excel
class Applicant_Details(models.Model):
    team_name = models.CharField(
        max_length=100,
        null=False
    )
    team_leader = models.CharField(
        max_length=100,
        null=False
    )
    event_name = models.CharField(
        max_length= 50,
        null=False
    )
    team_no = models.CharField(
        max_length=100,
        null=False,
        default="Team 1"
    )
    ############### participant 1
    participant_1_Name = models.CharField(
        max_length=50,
        null=False
    )
    participant_1_class = models.CharField(
        max_length=100,
        null=True
    )
    participant_1_rollno = models.CharField(
        max_length=100,
        null=True
    )
    participant_1_contactno = models.CharField(
        max_length=100,
        null=True
    )
    ############### participant 2
    participant_2_Name = models.CharField(
        max_length=50,
        null=False
        
    )
    participant_2_class = models.CharField(
        max_length=100,
        null=True
    )
    participant_2_rollno = models.CharField(
        max_length=100,
        null=True
    )
    participant_2_contactno = models.CharField(
        max_length=100,
        null=True
    )
    ############### participant 3
    participant_3_Name = models.CharField(
        max_length=50,
        null=True
    )
    participant_3_class = models.CharField(
        max_length=100,
        null=True
    )
    participant_3_rollno = models.CharField(
        max_length=100,
        null=True
    )
    participant_3_contactno = models.CharField(
        max_length=100,
        null=True
    )
    ############### participant 4
    participant_4_Name = models.CharField(
        max_length=50,
        null=True
    )
    participant_4_class = models.CharField(
        max_length=100,
        null=True
    )
    participant_4_rollno = models.CharField(
        max_length=100,
        null=True
    )
    participant_4_contactno = models.CharField(
        max_length=100,
        null=True
    )
    ############### participant 5
    participant_5_Name = models.CharField(
        max_length=50,
        null=True
    )
    participant_5_class = models.CharField(
        max_length=100,
        null=True
    )
    participant_5_rollno = models.CharField(
        max_length=100,
        null=True
    )
    participant_5_contactno = models.CharField(
        max_length=100,
        null=True
    )
    ############### participant 6
    participant_6_Name = models.CharField(
        max_length=50,
        null=True
    )
    participant_6_class = models.CharField(
        max_length=100,
        null=True
    )
    participant_6_rollno = models.CharField(
        max_length=100,
        null=True
    )
    participant_6_contactno = models.CharField(
        max_length=100,
        null=True
    )
    ############### participant 7
    participant_7_Name = models.CharField(
        max_length=50,
        null=True
    )
    participant_7_class = models.CharField(
        max_length=100,
        null=True
    )
    participant_7_rollno = models.CharField(
        max_length=100,
        null=True
    )
    participant_7_contactno = models.CharField(
        max_length=100,
        null=True
    )
    