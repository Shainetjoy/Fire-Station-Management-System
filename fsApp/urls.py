from django.urls import path
from fsApp import views,Adminviews

urlpatterns = [
path('',views.index,name='fsIndex'),
path('fsSignIn',views.fsSignIn,name='fsSignIn'),
path('fsSignUp',views.fsSignUp,name='fsSignUp'),
path('fsAdminIndex',views.fsAdminIndex,name='fsAdminIndex'),
path('fsGuestIndex',views.fsGuestIndex,name='fsGuestIndex'),
path('viewGuest',Adminviews.viewGuest,name='viewGuest'),
path('incidentRegister',Adminviews.incidentReg,name='incidentRegister'),
path('viewIncident',Adminviews.viewIncident,name='viewIncident'),
path('deleteGuest/<int:user_id>/',Adminviews.deleteGuest,name='deleteGuest'),

]