from django.shortcuts import render,redirect
from.forms import GuestRegister,UserRegister
from django.contrib import messages,auth
from django.contrib.auth import login, logout
# Create your views here.
def index(request):
    return render(request,"fsIndex.html")


def fsSignIn(request):
    if request.method == 'POST':
        username = request.POST.get('first')
        password = request.POST.get('password')
        user = auth.authenticate(username = username,password = password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('fsAdminIndex')
        elif user is not None and user.is_Guest:
            login(request,user)
            return redirect('fsGuestIndex')
        else:
            messages.info(request,"You Are Not A Registered User ")
    return render(request,"fsSignIn.html")



def fsSignUp(request):
    UserReg = UserRegister()
    GuestReg = GuestRegister()

    if request.method == 'POST':
        UserReg = UserRegister(request.POST)
        GuestReg = GuestRegister(request.POST)
        if UserReg.is_valid() and GuestReg.is_valid():
            user = UserReg.save(commit=False)
            user.is_Guest = True
            user.save()
            gust = GuestReg.save(commit=False)
            gust.user = user
            gust.save()
            messages.info(request,"Invalid credentials")
            return redirect('fsSignIn')
    return render(request,'fsSignUp.html',{'UserReg':UserReg,"GuestReg":GuestReg})


def fsAdminIndex(request):
    return render(request,'fsAdminIndex.html')


def fsGuestIndex(request):
    return render(request,'fsGuestIndex.html')



