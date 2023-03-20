from django.urls import path
from chenai.views import *

app_name='chenai'

urlpatterns=[
    path('chenai/',chenai,name='chenai'),
    path('tamil/',tamil,name='tamil')
]