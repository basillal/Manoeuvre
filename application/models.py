from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

# Login details
class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        primary_key=True
    )
    username = models.CharField(
        max_length=100,
        null = True
    )
    team_name = models.CharField(
        max_length=100,
        null = True
    )
    team_leader2= models.CharField(
        max_length= 50,
        null = True
    )
    password = models.CharField(
        max_length= 50,
        null = False
    )
    is_team = models.BooleanField(default=False)
    is_oncontrol = models.BooleanField(default=False)
    

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_team

    def has_module_perms(self, app_label):
        return True
    





class Participants(models.Model):
    team_name = models.CharField(
        max_length=100,
        null=False,
    )
    team_leader = models.CharField(
        max_length=100,
        null=False,
    )
    event_name = models.CharField(
        max_length= 50,
        null=False,
    )
    team_no = models.CharField(
        max_length=100,
        null=False,
        default="Team 1"
    )
    participant_name = models.CharField(
        max_length=100,
        null=False,
    )
    register_number = models.CharField(
        max_length=15,
        null=False,
   )


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
    EVENT_CHOICES = [
        ('IT Quiz', 'IT Quiz'),
        ('IT Manager', 'IT Manager'),
        ('Gaming', 'Gaming'),
        ('Hackathon', 'Hackathon'),
        ('Treasure Hunt', 'Treasure Hunt'),
        ('Web Designing', 'Web Designing'),
        ('Coding & Debugging', 'Coding & Debugging'),
        ('Short Film', 'Short Film'),
    ]
    event_name = models.CharField(
        max_length= 50,
        choices=EVENT_CHOICES,
        null=False,

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
    ###########################################################################   individual database    ######################################################

# ###################################                               Applicant details IT Manager
class IT_manager_Details(models.Model):
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
        default="IT Manager",
        null=False,
        editable=False,
    )
    TEAM_CHOICES = [
        ('1', 'Team 1'),
        ('2', 'Team 2'),
        ('3', 'Team 3'),
        ('4', 'Team 4'),
        ('5', 'Team 5'),
        ('6', 'Team 6')
    ]
    team_no = models.CharField(
        max_length=100,
        null=False,
        choices=TEAM_CHOICES
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



  ####################################  #                          Applicant details IT Quiz
class IT_Quiz_Details(models.Model):
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
        default="IT Quiz",
        null=False,
        editable=False,

    )
    TEAM_CHOICES = [
        ('1', 'Team 1'),
        ('2', 'Team 2'),
        ('3', 'Team 3'),
        ('4', 'Team 4'),
        ('5', 'Team 5'),
        ('6', 'Team 6')
    ]
    team_no = models.CharField(
        max_length=100,
        null=False,
        choices=TEAM_CHOICES
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


####################################                           Applicant details Gaming
class Gaming_Details(models.Model):
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
        default="Gaming",
        null=False,
        editable=False,
    )
    team_no = models.CharField(
        max_length=100,
        null=False,
        default="1",
        editable=False,
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




  ####################################  #                       Applicant details Web Designing
class Web_Designing_Details(models.Model):
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
        default="Web Designing",
        null=False,
        editable=False,
        
    )
    TEAM_CHOICES = [
        ('1', 'Team 1'),
        ('2', 'Team 2'),
        ('3', 'Team 3'),
        ('4', 'Team 4'),
        ('5', 'Team 5'),
        ('6', 'Team 6')
    ]
    team_no = models.CharField(
        max_length=100,
        null=False,
        choices=TEAM_CHOICES
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





####################################                       Applicant details Short Film
class Short_film_Details(models.Model):
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
        default="Short Film",
        null=False,
    )
    team_no = models.CharField(
        max_length=100,
        null=False,
        default="Team 1"
    )
    ############### participant 1   # we are only keeping one participant bcoz in this event everyone will participate
    participant_1_Name = models.CharField(
        max_length=500,
        null=False
    )
    participant_1_class = models.CharField(
        max_length=50,
        null=True
    )
    participant_1_rollno = models.CharField(
        max_length=1000,
        null=True
    )
    participant_1_contactno = models.CharField(
        max_length=500,
        null=True
    )




####################################                             Applicant details treasure hunt
#1 team from each grp and 6 members will there in each team
class Treasure_hunt_Details(models.Model):
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
        default="Treasure Hunt",
        null=False,
        editable=False,
    )
    team_no = models.CharField(
        max_length=100,
        null=False,
        default="1",
        editable=False,
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




####################################                       Applicant details Coding
###  in this event total 6 members will be there from each team
#  so each member will be a team only ... so from one grp 6 team will be there with 1 participant each

class Coding_Details(models.Model):
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
        default="Coding",
        null=False,
        editable=False,
    )
    TEAM_CHOICES = [
        ('1', 'Team 1'),
        ('2', 'Team 2'),
        ('3', 'Team 3'),
        ('4', 'Team 4'),
        ('5', 'Team 5'),
        ('6', 'Team 6')
    ]
    team_no = models.CharField(
        max_length=100,
        null=False,
        choices=TEAM_CHOICES
    )
    ############### participant 1   
    participant_1_Name = models.CharField(
        max_length=500,
        null=False
    )
    participant_1_class = models.CharField(
        max_length=50,
        null=False
    )
    participant_1_rollno = models.CharField(
        max_length=1000,
        null=False
    )
    participant_1_contactno = models.CharField(
        max_length=500,
        null=False
    )




  ####################################  #                       Applicant details Hackathon
  # 2 team from each grp with 2 particpant each in a team
class Hackathon_Details(models.Model):
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
        default="Hackathon",
        null=False,
        editable= False,

    )
    TEAM_CHOICES = [
        ('1', 'Team 1'),
        ('2', 'Team 2'),
        ('3', 'Team 3'),
        ('4', 'Team 4'),
        ('5', 'Team 5'),
        ('6', 'Team 6')
    ]
    team_no = models.CharField(
        max_length=100,
        null=False,
        choices=TEAM_CHOICES
    )
    ############### participant 1
    participant_1_Name = models.CharField(
        max_length=50,
        null=False
    )
    participant_1_class = models.CharField(
        max_length=100,
        null=False
    )
    participant_1_rollno = models.CharField(
        max_length=100,
        null=False
    )
    participant_1_contactno = models.CharField(
        max_length=100,
        null=False
    )
    ############### participant 2
    participant_2_Name = models.CharField(
        max_length=50,
        null=False
        
    )
    participant_2_class = models.CharField(
        max_length=100,
        null=False
    )
    participant_2_rollno = models.CharField(
        max_length=100,
        null=False
    )
    participant_2_contactno = models.CharField(
        max_length=100,
        null=False
    )