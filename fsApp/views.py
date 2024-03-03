from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"fsIndex.html")


def fsSignIn(request):
    return render(request,"fsSignIn.html")