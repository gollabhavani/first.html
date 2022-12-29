from django.urls import path
from app2.views import *
app_nqme='something2'


urlpatterns={
    path('second/',second,name='second'),
}