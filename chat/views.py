from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        myuser = User.objects.create_user(username, password, confirmpassword)
        myuser.First_Name = firstname
        myuser.Last_Name = lastname

        myuser.save()

        messages.success(request, 'Your Account has been created')

        return redirect('signin')
    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            firstname = user.firstname
            return render(request, 'room.html', {'firstname': firstname})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, 'signin.html')

def signout(request):
    return render(request, 'signout.html')


