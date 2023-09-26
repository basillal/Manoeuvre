from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ApplicantForm,ParticipantForm,shortfilmForm, WebdesignForm ,itmanagerForm,itquizForm,gamingForm,hackathonForm,tressureForm,codingForm, CreateUserForms
from .models import IT_manager_Details,IT_Quiz_Details,Hackathon_Details,Coding_Details,Treasure_hunt_Details,Gaming_Details,Short_film_Details,Web_Designing_Details



# ParticipantFormSet = formset_factory(ParticipantForm)

# Create your views here.
@login_required(login_url='login')
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



@login_required(login_url='login')
def registration(request, event_name):
    event=event_name
    print(event_name,event)

    if event == "ITManager":
        form = itmanagerForm()
        registered_students = IT_manager_Details.objects.filter(event_name = "IT Manager")  
        if request.method == 'POST':
            form = itmanagerForm(request.POST)
            if form.is_valid():
                form.save()  
                form = itmanagerForm()
                messages.info(request,'Registered Successfully')

               
                
                

        context = {
            'form': form,
            'event_name': event,
            'registered_students': registered_students,

            

        }    
               
        return render(request,'registration.html', context)
    elif event == "ITQuiz":
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
    elif event == "TreasureHunt":
        form = tressureForm()
        if request.method == 'POST':
            form = tressureForm(request.POST)
            if form.is_valid():
                form.save()            

        context = {
            'form': form
        }    
       
        return render(request,'registration.html', context)
    elif event == "Shortfilm":
        form = shortfilmForm()
        if request.method == 'POST':
            form = hackathonForm(request.POST)
            if form.is_valid():
                form.save()            

        context = {
            'form': form
        }    
       
        return render(request,'registration.html', context)
    elif event == "coding":
        form = codingForm()
        if request.method == 'POST':
            form = codingForm(request.POST)
            if form.is_valid():
                form.save()            

        context = {
            'form': form
        }    
       
        return render(request,'registration.html', context)
    elif event == "webdesign":
        form = WebdesignForm()
        if request.method == 'POST':
            form = WebdesignForm(request.POST)
            if form.is_valid():
                form.save()            

        context = {
            'form': form
        }    
       
        return render(request,'registration.html', context)





def loginPage(request):
   
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request,'username OR password is incorrect')
            return render(request,'auth/login.html')
        
    return render(request,'auth/login.html')

def logoutUser(request):
    logout(request)    
    return redirect('login')

