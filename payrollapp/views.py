
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    return  render(request,"home.html")

# usename Prince123 pass1
# pri pass

def loginu(request):

    if request.method == 'POST':
        user_name = request.POST['user_name']
        password1 = request.POST['password1']
        user = authenticate(username = user_name,password = password1)

        if user is not None:
            login(request,user)
            first_name = user.first_name
            return render(request,"home.html",{'first_name':first_name})
        else:
            messages.error(request,"bad credentials")
            return redirect('home')

    return render(request,"loginu.html")




def signup(request):
    if request.method == 'POST':
        # user_name = request.POST.get(user_name) or
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(user_name,email,password1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()

        messages.success(request,"your account has been created")
        return redirect('loginu')
        

    return render(request,"signup.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out succesfully")
    return redirect('home')

