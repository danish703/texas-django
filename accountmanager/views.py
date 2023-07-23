from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        u = request.POST["username"]
        f = request.POST["fname"]
        l = request.POST["lname"]
        p = request.POST.get("pass1")
        pc =  request.POST.get("pass2")

        if p == pc:
            user = User(username=u,first_name=f,last_name=l)
            user.set_password(p)
            user.save()
            return redirect('signin')
        else:
            errmsg = "Password and Password Confirmation does not match"
            return redirect('signup')


def signin(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        u = request.POST["username"]
        p = request.POST["pass1"]
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')



def  dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return redirect('signin')


def signout(request):
    logout(request)
    return redirect('signin')