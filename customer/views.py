from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer
from client.models import Client

def customer_list (request):
    customers = Customer.objects.all()
    clients = Client.objects.all()
    print(customers)
    return render(request, "customer_app/customer_list.html", {"customers": customers, "clients": clients})

def customer_create(request):
    print('wajahat')
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        client_id = request.POST.get('client')

        client = Client.objects.get(id=int(client_id))
    
        customer= Customer.objects.create(
            name=name,
            email=email,
            address=address,
            client=client
        )
        return JsonResponse({"message":" Customer successfully created"})
    return JsonResponse({"message": "Invalid request"})
