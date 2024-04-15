from django.urls import path
from app.views import client_list
from app.views import add_client
from app.views import edit_client
from app.views import client_detail
from app.views import delete_client
from app.views import index


urlpatterns = [
    path('', index, name='index'),
    path('add_client/', add_client, name='add_client'),
    path('list/', client_list, name='client_list'),
    path('edit_client/<int:client_id>/', edit_client, name='edit_client'),
    path('client_detail/<int:client_id>/', client_detail, name='client_detail'),
    path('delete_client/<int:client_id>/', delete_client, name='delete_client'),
]