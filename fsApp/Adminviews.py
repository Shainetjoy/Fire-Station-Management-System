from django.shortcuts import render,redirect
from fsApp.models import Guest



def viewGuest(request):
    GustsDtl = Guest.objects.all()
    return render(request,'admin/ViewGuests.html',{'GustsDtl':GustsDtl})



def deleteGuest(request,user_id):
    data = Guest.objects.get(user_id=user_id)
    data.delete()
    return redirect('viewGuest')





