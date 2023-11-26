from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered Succesfuly')
            return redirect('registration-url')
    else:
        form = RegistrationForm()


    return render(request, 'aunthentic/reegister.html', {"form":form})


