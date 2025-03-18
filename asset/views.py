from django.shortcuts import render
from django.http import JsonResponse
from .models import Asset
from sitee.models import Sitee

def asset_list(request):
    print("GET")
    print(request.GET)
    page = int(request.GET.get('page', 1))
    per_page = 3
    start = (page - 1)*per_page
    end= start + per_page

    total_assets = Asset.objects.count()

    assets = Asset.objects.select_related('sitee__customer__client').all()[start:end]
    print(assets)
    sitees = Sitee.objects.all()

    return render(request, 'asset/asset_list.html', {'assets': assets, 'current_page': page, 'total_pages': (total_assets + per_page - 1) // per_page })

def asset_create(request):
    print(request.POST)
    if request.method== 'POST':
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        address = request.POST.get('address')
        sitee_id = request.POST.get('sitee')

        sitee = Sitee.objects.get(id = sitee_id)

        Asset.objects.create(
            name= name,
            phone_num=phone_num,
            address=address,
            sitee=sitee
        )
        return JsonResponse({'message': 'Successfully added new asset'})
    return JsonResponse({'message': 'Invalid request'})


