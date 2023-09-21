from django.http import JsonResponse
from .models import Applicant_Details
from django.shortcuts import render,redirect
from .forms import ApplicantForm,ParticipantForm, WebdesignForm ,itmanagerForm,itquizForm,gamingForm,hackathonForm,tressureForm
# from .models import Participants  # Import your Participant model here
# from .forms import ParticipantForm  # Import your ParticipantForm here

# ParticipantFormSet = formset_factory(ParticipantForm)

# Create your views here.
def index(request):
    form = WebdesignForm()
    n = 0
    event_choices = [
        'IT Quiz','IT Manager','Gaming','Hackathon','Treasure Hunt','Web Designing','Coding & Debugging', 'Short Film', 
        ]
    context = {
        'form': form,
        'event_choices': event_choices,
        'n': n
    }
    if request.method == 'POST':
        form = WebdesignForm(request.POST)
        print("success")
        if form.is_valid():
            form.save()
            print("Data saved successfully")  # Add this line for debugging
            
            return JsonResponse({'message': 'Registration Successful'})
             # Redirect to a success page

    return render(request,'index.html', context)


##################
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
    



# #################################################################################################################
def itmanager(request):
    form = itmanagerForm()
    if request.method == 'POST':
        form = itmanagerForm(request.POST)
        if form.is_valid():
            form.save()            

    context = {
        'form': form
    }     
    
    return render(request,'itmanager.html', context)

