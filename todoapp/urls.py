from django.contrib import admin
from django.urls import path
from .views import loginpage,signup,home,logoutuser, createpost, viewposts, loadpost


urlpatterns = [
    path('signup/', signup,name='signup'),
    path('login/', loginpage,name='login'),
    path('logout/',logoutuser,name='logout'),
    
    path('',home,name='home'),

    path('createpost/',createpost, name='createpost'),
    path('viewposts/',viewposts, name='viewposts'),
    path('<id>/post/',loadpost,name='post')
]