from django.shortcuts import render,redirect
from fsApp.models import Guest
from .forms import Incident_register



def viewGuest(request):
    GustsDtl = Guest.objects.all()
    return render(request,'admin/ViewGuests.html',{'GustsDtl':GustsDtl})



def deleteGuest(request,user_id):
    data = Guest.objects.get(user_id=user_id)
    data.delete()
    return redirect('viewGuest')


def incidentReg(request):
    incidentREgistrstionForm = Incident_register()
    if request.method == 'POST':
        incidentREgistrstionForm = Incident_register(request.POST)
        if incidentREgistrstionForm.is_valid():
            incidentREgistrstionForm.save()
            return redirect('fsAdminIndex')

    return render(request,'admin/incidentRegister.html',{'incidentREgistrstionForm':incidentREgistrstionForm})





