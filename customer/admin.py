from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'client')


admin.site.register(Customer, CustomerAdmin)
