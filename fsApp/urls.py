from django.urls import path
from fsApp import views


path('',views.index,name='fsIndex'),
