from django import forms
from .models import Participants,Applicant_Details,Web_Designing_Details

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participants
        fields = ['team_name', 'team_leader', 'event_name', 'team_no', 'participant_name', 'register_number']
    team_name = forms.CharField(required=True)
    team_leader_name = forms.CharField(required=True)
    event_name = forms.CharField(required=True)
    team_no = forms.CharField(required=True)
    participant_name = forms.CharField(required=True)
    register_number = forms.CharField(required=True)


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant_Details
        fields = ['team_name', 'team_leader', 'event_name', 'team_no', 'participant_1_name', 'participant_1_rollno','participant_1_contactno','participant_1_class', 'participant_2_name', 'participant_2_rollno','participant_2_contactno','participant_2_class', 'participant_3_name', 'participant_3_rollno','participant_3_contactno','participant_3_class', 'participant_4_name', 'participant_4_rollno','participant_4_contactno','participant_4_class', 'participant_5_name', 'participant_5_rollno','participant_5_contactno','participant_5_class', 'participant_6_name', 'participant_6_rollno','participant_6_contactno','participant_6_class', 'participant_7_name', 'participant_7_rollno','participant_7_contactno','participant_7_class']
    team_name = forms.CharField(required=True)
    team_leader_name = forms.CharField(required=True)
    event_name = forms.CharField(required=True)
    team_no = forms.CharField(required=True)
    participant_1_name = forms.CharField(required=True)
    participant_1_rollno = forms.CharField(required=True)
    participant_1_contactno = forms.CharField(required=True)
    participant_1_class = forms.CharField(required=True)

    participant_2_name = forms.CharField(required=False)
    participant_2_rollno = forms.CharField(required=False)
    participant_2_contactno = forms.CharField(required=False)
    participant_2_class = forms.CharField(required=False)
    
    participant_3_name = forms.CharField(required=False)
    participant_3_rollno = forms.CharField(required=False)
    participant_3_contactno = forms.CharField(required=False)
    participant_3_class = forms.CharField(required=False)
    
    participant_4_name = forms.CharField(required=False)
    participant_4_rollno = forms.CharField(required=False)
    participant_4_contactno = forms.CharField(required=False)
    participant_4_class = forms.CharField(required=False)
    
    participant_5_name = forms.CharField(required=False)
    participant_5_rollno = forms.CharField(required=False)
    participant_5_contactno = forms.CharField(required=False)
    participant_5_class = forms.CharField(required=False)
    
    participant_6_name = forms.CharField(required=False)
    participant_6_rollno = forms.CharField(required=False)
    participant_6_contactno = forms.CharField(required=False)
    participant_6_class = forms.CharField(required=False)
    
    participant_7_name = forms.CharField(required=False)
    participant_7_rollno = forms.CharField(required=False)
    participant_7_contactno = forms.CharField(required=False)
    participant_7_class = forms.CharField(required=False)

class WebdesignForm(forms.ModelForm):
    class Meta:
        model = Web_Designing_Details
        fields = '__all__'

        labels = {
            'team_leader': 'King'
            
        }