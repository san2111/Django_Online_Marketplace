from django.contrib import admin
from django.urls import path ,include

from django.conf import settings
from django.conf.urls.static import static

from app.views import index ,contact



urlpatterns = [
    path('',index, name='index'),
    path('contact/',contact, name='contact'),
    path('admin/', admin.site.urls),
    path('items/',include('items.urls')),
 ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
