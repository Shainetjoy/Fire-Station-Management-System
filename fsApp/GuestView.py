from django.shortcuts import render

from fsApp.models import incident


def GustIncedentView(request):
    gustInciddentView = incident.objects.fillter()


    return render(request,'guest/GustincidentView.html')



def guestviewIncident(request):
    allIncident = incident.objects.all()
    return render(request, 'guest/viewIncident.html', {'allIncident': allIncident})