from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):
    model = CarMake
    extra = 5



admin.site.register(CarMake)
admin.site.register(CarModel)
