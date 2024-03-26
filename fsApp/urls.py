from django.urls import path
from fsApp import views,Adminviews,GuestView

urlpatterns = [
path('',views.index,name='fsIndex'),
path('fsSignIn',views.fsSignIn,name='fsSignIn'),
path('fsSignUp',views.fsSignUp,name='fsSignUp'),
path('log_out',views.log_out,name='log_out'),
path('fsAdminIndex',views.fsAdminIndex,name='fsAdminIndex'),
path('fsGuestIndex',views.fsGuestIndex,name='fsGuestIndex'),
path('viewGuest',Adminviews.viewGuest,name='viewGuest'),
path('incidentRegister',Adminviews.incidentReg,name='incidentRegister'),
path('viewIncident',Adminviews.viewIncident,name='viewIncident'),
path('deleteIncident<int:id>',Adminviews.deleteIncident,name='deleteIncident'),
path('updateIncident<int:id>',Adminviews.updateIncident,name='updateIncident'),
path('resourceAllocation',Adminviews.resourceAllocation,name='resourceAllocation'),
path('allowcationBtn1',Adminviews.allowcationBtn1,name='allowcationBtn1'),
path('allowcationBtn2',Adminviews.allowcationBtn2,name='allowcationBtn2'),
path('allowcationBtn3',Adminviews.allowcationBtn3,name='allowcationBtn3'),
path('Personsfun',Adminviews.Personsfun,name='Personsfun'),
path('addPerson',Adminviews.addPerson,name='addPerson'),
path('viewPerson',Adminviews.viewPerson,name='viewPerson'),
path('deletePerson/<int:id>/',Adminviews.deletePerson,name='deletePerson'),
path('UpdatePerson/<int:id>/',Adminviews.UpdatePerson,name='UpdatePerson'),
path('deleteGuest/<int:user_id>/',Adminviews.deleteGuest,name='deleteGuest'),
path('deleteequipment/<int:id>/',Adminviews.deleteequipment,name='deleteequipment'),
path('Maintenance',Adminviews.Maintenance,name='Maintenance'),
path('Addequipment',Adminviews.AddequipmentFun,name='Addequipment'),
path('viewEquipment',Adminviews.viewEquipment,name='viewEquipment'),
path('UpdateEquipments/<int:id>/',Adminviews.UpdateEquipments,name='UpdateEquipments'),
path('guestviewIncident',GuestView.guestviewIncident,name='guestviewIncident'),
path('approveGuest/<int:id>',Adminviews.approveGuest,name='approveGuest'),


]