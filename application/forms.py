from django import forms
from .models import Participants

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participants
        fields = ['team_name', 'team_leader', 'event_name', 'team_no', 'participant_name', 'register_number']