from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Client
from django.contrib import messages


def client_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        address = request.POST.get('address')

        if not name or not phone_num:
            messages.error(request, 'Name and phone number is required!')
            return redirect(client_create)
        
        Client.objects.create(
            name=name,
            phone_num=phone_num,
            address=address
        )
        messages.success(request,'Created Successfuly!')
        return redirect('client_list')
    
    return render(request, 'client_app/create.html')


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_app/client_list.html',{'clients':clients})

def client_list_in_json(request):
    clients = Client.objects.all().values("id", "name", "phone_num", "address")  # Get data as a dictionary
    print(f"clients = {clients}")
    data = {
      "clients": list(clients)
    }
    return JsonResponse(data, safe=False)


def client_update(request, id):
    client = get_object_or_404(Client, id=id)

    if request.method == 'POST':
        client.name = request.POST.get('name')
        client.phone_num = request.POST.get('phone_num')
        client.address = request.POST.get('address')
        client.save()
        return redirect('client_list')
    
    return render(request, 'client_app/update.html',{'client':client})

def client_delete(request, id):
    client= Client.objects.get(id=id)

    if request.method =="POST":
        client.delete()
        return redirect('client_list')
    
    return render(request, "client_app/delete.html", {'client': client})