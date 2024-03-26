from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_Guest = models.BooleanField(default=False)




class Guest(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Guest')
    Name = models.CharField(max_length=20)
    Phone = models.CharField(max_length=10)
    Email = models.EmailField()
    approval_status =models.IntegerField(default=0)

    def __str__(self):
        return self.Name

IncidentType = (
    ('Fire','Fire'),
    ('Rescue','Rescue'),
    ('Medical Emergency','Medical Emergency'))

class incident(models.Model):
    Incident_Name = models.CharField(max_length=100)
    Incident_Type = models.CharField(max_length=100,choices=IncidentType)
    Incident_Location = models.CharField(max_length=100)
    Date_and_Time_of_Incident = models.DateField(auto_now=True)
    Weather_Conditions = models.CharField(max_length=200)
    Names_and_IDsof_Responding_Personnel =models.CharField(max_length=100)
    Roles_and_Responsibilities_Assigned = models.CharField(max_length=200)
    Injured_or_Affected_Individuals = models.CharField(max_length=100)
    Equipment_Used = models.CharField(max_length=100)
    images = models.ImageField(upload_to='IncidentImage/')

    def __str__(self):
        return self.Incident_Name



class Persons(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=10)
    role = models.CharField(max_length=100)
    certification = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()
    shift = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class Addequipment(models.Model):

    EquipmentID = models.CharField(max_length=100)
    EquipmentName = models.CharField(max_length=100)
    Equipment_Type = models.CharField(max_length=100)
    Manufacturer = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Serial_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField()
    Last_Maintenance_Date = models.DateField()
    Next_Maintenance_Due = models.DateField()
    Maintenance_Schedule =models.DateField()
    Maintenance_Status = models.CharField(max_length=100)
    Next_Inspection_Date = models.DateField()
    Compliance_Status = models.CharField(max_length=100)




