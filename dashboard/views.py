from django.shortcuts import render, redirect
from client.views import client_list

def dashboard(request):
    print('wajahat')
    if request.method=="POST":
        return redirect('client_list')
    
    return render(request, 'dashboard/dashboard.html')
