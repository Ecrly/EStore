from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CustomerOrder, CustomerAdmin)