from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ApplicantForm,ParticipantForm,shortfilmForm, WebdesignForm ,itmanagerForm,itquizForm,gamingForm,hackathonForm,tressureForm,codingForm, CreateUserForms
from .models import IT_manager_Details,IT_Quiz_Details,Hackathon_Details,Coding_Details,Treasure_hunt_Details,Gaming_Details,Short_film_Details,Web_Designing_Details



# ParticipantFormSet = formset_factory(ParticipantForm)

# Create your views here.
# @login_required(login_url='login')
def index(request):
    form = WebdesignForm()
    n = 0
    event_choices = [
        'IT Quiz','IT Manager','Gaming','Hackathon','Treasure Hunt','Web Designing','Coding & Debugging', 'Short Film', 
        ]
    context = {
        'form': form,
        'event_choices': event_choices,       
    }
    if request.method == 'POST':
        form = WebdesignForm(request.POST)
        print("success")
        if form.is_valid():
            form.save()           
            
            return JsonResponse({'message': 'Registration Successful'})
             # Redirect to a success page

    return render(request,'index.html', context)   



# @login_required(login_url='login')
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
                messages.info(request,'Successfully')

               
                
                

        context = {
            'form': form,
            'event_name': event,
            'registered_students': registered_students,

            

        }    
               
        return render(request,'registration.html', context)
    elif event == "ITQuiz":
        form = itquizForm()
        registered_students = IT_Quiz_Details.objects.filter(event_name = "IT Quiz")  
        if request.method == 'POST':
            form = itquizForm(request.POST)
            if form.is_valid():
                form.save()    
                form = itquizForm()
                messages.info(request,'Successfully')        

        context = {
            'form': form,
            'event_name': event,
            'registered_students': registered_students,
        }    
       
        return render(request,'registration.html', context)
    elif event == "Gaming":
        form = gamingForm()
        registered_students = Gaming_Details.objects.filter(event_name = "Gaming")  
        if request.method == 'POST':
            form = gamingForm(request.POST)
            if form.is_valid():
                form.save() 
                form = gamingForm()
                messages.info(request,'Successfully')           

        context = {
            'form': form,
            'event_name': event,
            'registered_students': registered_students,
        }    
       
        return render(request,'registration.html', context)
    elif event == "Hackathon":
        form = hackathonForm()
        registered_students = Hackathon_Details.objects.filter(event_name = "Hackathon")  
        if request.method == 'POST':
            form = hackathonForm(request.POST)
            if form.is_valid():
                form.save()  
                form = hackathonForm()
                messages.info(request,'Successfully')             

        context = {
            'form': form,
            'event_name': event,
            'registered_students': registered_students,
        }    
       
        return render(request,'registration.html', context)
    elif event == "TreasureHunt":
        form = tressureForm()
        registered_students = Treasure_hunt_Details.objects.filter(event_name = "Treasure Hunt")  
        if request.method == 'POST':
            form = tressureForm(request.POST)
            if form.is_valid():
                form.save() 
                form = tressureForm()
                messages.info(request,'Successfully')             

        context = {
            'form': form,
            'event_name': event,
            'registered_students': registered_students,
        }    
       
        return render(request,'registration.html', context)
    elif event == "Shortfilm":
        form = shortfilmForm()
        registered_students = Short_film_Details.objects.filter(event_name = "Short Film")  
        if request.method == 'POST':
            form = shortfilmForm(request.POST)
            if form.is_valid():
                form.save() 
                form = shortfilmForm()
                messages.info(request,'Successfully')   
                          

        context = {
            'form': form,
            'event_name': event,
            'registered_students': registered_students,
        }    
       
        return render(request,'registration.html', context)
    elif event == "coding":
        form = codingForm()
        registered_students = Coding_Details.objects.filter(event_name = "Coding")  
        if request.method == 'POST':
            form = codingForm(request.POST)
            if form.is_valid():
                form.save() 
                form = codingForm()
                messages.info(request,'Successfully')   
                                     

        context = {
            'form': form,
            'event_name': event,
            'registered_students': registered_students,
        }    
       
        return render(request,'registration.html', context)
    elif event == "webdesign":
        form = WebdesignForm()
        registered_students = Web_Designing_Details.objects.filter(event_name = "Web Designing")  
        if request.method == 'POST':
            form = WebdesignForm(request.POST)
            if form.is_valid():
                form.save()  
                form = WebdesignForm()
                messages.info(request,'Successfully')           

        context = {
            'form': form,
            'event_name': event,
            'registered_students': registered_students,
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

