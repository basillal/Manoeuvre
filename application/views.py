# registration_app/views.py
from django.shortcuts import render, redirect
from .forms import ApplicantForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def registrationpage_view(request):
    print("the register page called")
    return render(request,'registration.html')


def registration_view(request):
    print("the function is called")
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")  # Add this line for debugging
            return redirect('success_page')  # Redirect to a success page
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = ApplicantForm()
    return render(request, 'registration.html', {'form': form})



def success_page(request):
    return render(request, 'success.html')
