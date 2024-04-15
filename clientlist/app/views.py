from django.shortcuts import render
from django.shortcuts import redirect
from app.models import Client
from .forms import ClientForm


def index(request):
    return render(request, 'index.html')


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})


def add_client(request):
    return render(request, 'clients/add_client.html')


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'clients/add_client.html', {'form': form})