from django.contrib import admin
from .models import Animal, Customer, Locate

# Register your models here.

admin.site.register(Animal)
admin.site.register(Customer)
admin.site.register(Locate)