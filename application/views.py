from django.http import JsonResponse
from django.shortcuts import render
from django.forms import formset_factory
from .models import Participants  # Import your Participant model here
from .forms import ParticipantForm  # Import your ParticipantForm here

# ParticipantFormSet = formset_factory(ParticipantForm)

# Create your views here.
def index(request):
    return render(request,'index.html')

def event_registration(request):
    if request.method == 'POST':
        # Access and process form data
        print(request.POST.dict())
        event_name = request.POST.get('event_name')
        print(event_name)

        return JsonResponse({'message': 'Registration Successful'})
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Invalid Request Method'}, status=405)