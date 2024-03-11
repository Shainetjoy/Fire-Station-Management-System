from django.urls import path
from fsApp import views

urlpatterns = [
path('',views.index,name='fsIndex'),
path('fsSignIn',views.fsSignIn,name='fsSignIn'),
path('fsSignUp',views.fsSignUp,name='fsSignUp'),
path('fsAdminIndex',views.fsAdminIndex,name='fsAdminIndex'),
path('fsGuestIndex',views.fsGuestIndex,name='fsGuestIndex'),

]