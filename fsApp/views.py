from django.shortcuts import render
from.forms import GuestRegister,UserRegister
# Create your views here.
def index(request):
    return render(request,"fsIndex.html")


def fsSignIn(request):
    return render(request,"fsSignIn.html")



def fsSignUp(request):
    UserReg =UserRegister()
    GuestReg = GuestRegister()
    return render(request,'fsSignUp.html',{'UserReg':UserReg,"GuestReg":GuestReg})


def fsAdminIndex(request):
    return render(request,'fsAdminIndex.html')


def fsGuestIndex(request):
    return render(request,'fsGuestIndex.html')