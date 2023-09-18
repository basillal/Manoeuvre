# registration_app/forms.py
from django import forms
from .models import Applicant_Details

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant_Details
        fields = ['team_name', 'team_leader', 'event_name', 'team_no', 'participant_1_Name', 'participant_1_class', 'participant_1_rollno', 'participant_1_contactno']

    # Add required field validation for each field
    team_name = forms.CharField(required=True)
    team_leader = forms.CharField(required=True)
    event_name = forms.CharField(required=True)
    team_no = forms.CharField(required=True)
    participant_1_Name = forms.CharField(required=True)
    participant_1_class = forms.CharField(required=True)
    participant_1_rollno = forms.CharField(required=True)
    participant_1_contactno = forms.CharField(required=True)

