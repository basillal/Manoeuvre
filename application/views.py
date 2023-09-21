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




    


















def registration(request, event_name):
    event=event_name
    print(event_name,event)
    if event == "ITManager":
        form = itmanagerForm()
        if request.method == 'POST':
            form = itmanagerForm(request.POST)
            if form.is_valid():
                form.save()            

        context = {
            'form': form
        }    
        return redirect('registration')
       
        return render(request,'registration.html', context)
    elif event == "IT Quiz":
        form = itquizForm()
        if request.method == 'POST':
            form = itquizForm(request.POST)
            if form.is_valid():
                form.save()            

        context = {
            'form': form
        }    
       
        return render(request,'registration.html', context)
    elif event == "Gaming":
        form = gamingForm()
        if request.method == 'POST':
            form = gamingForm(request.POST)
            if form.is_valid():
                form.save()            

        context = {
            'form': form
        }    
       
        return render(request,'registration.html', context)
    elif event == "Hackathon":
        form = hackathonForm()
        if request.method == 'POST':
            form = hackathonForm(request.POST)
            if form.is_valid():
                form.save()            

        context = {
            'form': form
        }    
       
        return render(request,'registration.html', context)
    elif event == "Treasure Hunt":
        form = tressureForm()
        if request.method == 'POST':
            form = tressureForm(request.POST)
            if form.is_valid():
                form.save()            

        context = {
            'form': form
        }    
       
        return render(request,'registration.html', context)
    elif event == "Hackathon":
        form = hackathonForm()
        if request.method == 'POST':
            form = hackathonForm(request.POST)
            if form.is_valid():
                form.save()            

        context = {
            'form': form
        }    
       
        return render(request,'registration.html', context)