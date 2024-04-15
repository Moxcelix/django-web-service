from django.contrib import admin
from django.urls import path
from app.views import client_list
from app.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('list/', client_list, name='client_list'),
]