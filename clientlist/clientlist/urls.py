from django.urls import path
from app.views import client_list
from app.views import add_client
from app.views import index


urlpatterns = [
    path('', index, name='index'),
    path('list/', client_list, name='client_list'),
    path('add_client/', add_client, name='add_client'),
]