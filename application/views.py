from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import ApplicantForm,ParticipantForm, WebdesignForm
# from .models import Participants  # Import your Participant model here
# from .forms import ParticipantForm  # Import your ParticipantForm here

# ParticipantFormSet = formset_factory(ParticipantForm)

# Create your views here.
def index(request):
    form = WebdesignForm()
    context = {
        'form': form
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
    



def registration_view(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")  # Add this line for debugging
            
            return JsonResponse({'message': 'Registration Successful'})
             # Redirect to a success page
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = ApplicantForm()
    return render(request, 'registration.html', {'form': form})

