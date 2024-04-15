from django.shortcuts import render
from app.models import Client

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})


def index(request):
    return render(request, 'index.html')