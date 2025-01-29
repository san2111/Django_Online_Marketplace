from django.contrib import admin
from django.urls import path

from app.views import index ,contact



urlpatterns = [
    path('',index, name='index'),
     path('contact/',contact, name='contact'),
    path('admin/', admin.site.urls),
]
