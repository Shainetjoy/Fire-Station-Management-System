from django.contrib import admin

from fsApp import models

# Register your models here.
admin.site.register(models.Guest)
admin.site.register(models.User)
admin.site.register(models.incident)
admin.site.register(models.Persons)
admin.site.register(models.Addequipment)
