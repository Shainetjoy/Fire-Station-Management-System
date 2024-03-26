from django.shortcuts import render

from fsApp.models import incident, Guest


def GustIncedentView(request):
    gustInciddentView = incident.objects.fillter()
    return render(request,'guest/GustincidentView.html')



def guestviewIncident(request):
    allIncident = incident.objects.all()
    # u = request.user.id
    # customer = Guest.objects.filter(user__id=u).values()
    # customer_name = customer[0]['Name']
    return render(request, 'guest/viewIncident.html', {'allIncident': allIncident})