from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
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


def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/edit_client.html', {'form': form})


def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'clients/client_detail.html', {'client': client})


def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'clients/client_list.html', {'client': client})