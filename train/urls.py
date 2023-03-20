from django.urls import path
from train.views import *

app_name='train'

urlpatterns=[
    path('mumbai/',mumbai,name='mumbai'),
    path('bharath/',bharath,name='bharath')
]