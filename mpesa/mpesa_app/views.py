from django.shortcuts import render, redirect
from. models import Players
from django.contrib.auth.models import User, auth
# Create your views here.
def home(request):

    winners=Players.objects.all()

    return render(request, 'home.html', {'winners':winners})

def register(request):
    if request.method =='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']


        x=User.objects.create_user(username=username, first_name=first_name, last_name= last_name, email=email,password=password1)
        x.save()
        print('user created')
        return redirect("login")


    else:    

        return render(request, 'register.html')



    


def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']


        x=auth.authenticate(username=username, password=password)

        if x is not None:
            auth.login(request, x)
            return redirect('dashboard')
        else:
            print("not logged in")
            return redirect('login')


    return render(request, 'login.html')


def dashboard(request):
    return render(request,'dashboard.html')



def logout(request):
    auth.logout(request)
    return redirect('home')

def deposit(request):
    return render(request, 'depositpopup.html')


