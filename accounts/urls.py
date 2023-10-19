from django.urls import path
from .views import *

urlpatterns = [

    # CRUD Users
    path('login/', login_request, name= 'Login'),
    path('register/', register, name= 'SignUp'),
    path('logout/', logout_request, name= 'Logout'),
    path('edit/', edit_user, name= 'Edit')
]