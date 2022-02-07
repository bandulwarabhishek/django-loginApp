from django.shortcuts import render, redirect, HttpResponseRedirect
from users.models import Member #models.py
from .forms import UserRegistrationForm
 
# Create your views here.
def index(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'index.html')
 
def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')
 
def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)