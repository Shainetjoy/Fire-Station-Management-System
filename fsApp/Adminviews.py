from django.shortcuts import render, redirect
from fsApp.models import Guest, incident,Persons,Addequipment
from .forms import Incident_register,AddnewPerson,AddequipmentForm
from django.contrib import messages


def viewGuest(request):
    GustsDtl = Guest.objects.all()
    return render(request, 'admin/ViewGuests.html', {'GustsDtl': GustsDtl})


def deleteGuest(request, user_id):
    data = Guest.objects.get(user_id=user_id)
    data.delete()
    return redirect('viewGuest')


def incidentReg(request):
    incidentREgistrstionForm = Incident_register()
    if request.method == 'POST':
        incidentREgistrstionForm = Incident_register(request.POST, request.FILES)
        print(incidentREgistrstionForm, "rrrrrrrrrrrrr")
        if incidentREgistrstionForm.is_valid():
            incidentREgistrstionForm.save()
            return redirect('fsAdminIndex')
    return render(request, 'admin/incidentRegister.html', {'incidentREgistrstionForm': incidentREgistrstionForm})


def viewIncident(request):
    allIncident = incident.objects.all()
    return render(request, 'admin/viewIncident.html', {'allIncident': allIncident})
def deleteIncident(request,id):
    data = incident.objects.get(id=id)
    data.delete()
    return redirect('viewIncident')

def updateIncident(request,id):
    upIncident = incident.objects.get(id = id)
    incidentREgistrstionForm = Incident_register(instance=upIncident)
    if request.method == 'POST':
        incidentREgistrstionForm = Incident_register(request.POST,instance=upIncident)
        if incidentREgistrstionForm.is_valid():
            incidentREgistrstionForm.save()
            return redirect('viewIncident')
    return render(request,'admin/updateincident.html',{'incidentREgistrstionForm':incidentREgistrstionForm})
def resourceAllocation(request):
    return render(request, 'admin/resourceAllocation.html')


def allowcationBtn1(request):
    messages.success(request, 'personal Resource Allocated Successfully')
    return render(request, 'admin/resourceAllocation.html')


def allowcationBtn2(request):
    messages.success(request, 'Equipment Resource Allocated Successfully')
    return render(request, 'admin/resourceAllocation.html')


def allowcationBtn3(request):
    messages.success(request, 'Vehicles Resource Allocated Successfully')
    return render(request, 'admin/resourceAllocation.html')


def Personsfun(request):
    return render(request, 'admin/person.html')


def addPerson(request):
    AddPersonForm = AddnewPerson()
    if request.method == 'POST':
        AddPersonForm = AddnewPerson(request.POST)
        if AddPersonForm.is_valid():
            AddPersonForm.save()
            return redirect('viewPerson')
    return render(request, 'admin/Addperson.html', {'AddPersonForm': AddPersonForm})

def viewPerson(request):
    allPersons = Persons.objects.all()
    return render(request,'admin/viewAllPersons.html',{'allPersons':allPersons})



def deletePerson(request , id):
    data = Persons.objects.get(id=id)
    data.delete()
    return redirect('viewPerson')


def UpdatePerson(request,id):
    updatePerson = Persons.objects.get(id = id)
    AddPersonForm = AddnewPerson(instance=updatePerson)
    if request.method == 'POST':
        AddPersonForm = AddnewPerson(request.POST,instance=updatePerson)
        if AddPersonForm.is_valid():
            AddPersonForm.save()
            return redirect('viewPerson')
    return render(request,'admin/updateperson.html',{'AddPersonForm':AddPersonForm})




def Maintenance(request):
    return render(request,'admin/Maintenance-main.html')



def AddequipmentFun(request):
    addEqupmentForm = AddequipmentForm()
    if request.method == 'POST':
        addEqupmentForm = AddequipmentForm(request.POST)
        if addEqupmentForm.is_valid():
            addEqupmentForm.save()
            return redirect('Maintenance')
    return render(request,'admin/AddequipmentPage.html',{"addEqupmentForm":addEqupmentForm})


def viewEquipment(request):
    allEqupements = Addequipment.objects.all()
    return render(request, 'admin/viewallEqupements.html', {'allEqupements': allEqupements})

def deleteequipment(request , id):
    data = Addequipment.objects.get(id=id)
    data.delete()
    return redirect('viewEquipment')

def UpdateEquipments(request ,id):
    eqpUpdate = Addequipment.objects.get(id=id)
    addEqupmentForm = AddequipmentForm(instance=eqpUpdate)
    if request.method == 'POST':
        addEqupmentForm = AddequipmentForm(request.POST,instance=eqpUpdate)
        if addEqupmentForm.is_valid():
            addEqupmentForm.save()
            return redirect('viewEquipment')
    return render(request,"admin/updateEqupment.html",{'addEqupmentForm':addEqupmentForm})




