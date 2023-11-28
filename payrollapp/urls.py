from django.urls import path,include
from .views import home,loginu,signout,signup

urlpatterns = [
    path('', home,name='home'),
    path('loginu', loginu,name = 'loginu'),
    path('signup' ,signup,name = 'signup'),
    path('signout', signout, name = 'signout'),
]