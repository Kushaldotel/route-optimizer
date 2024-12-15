from django.contrib import admin
from .models import FuelStop


class FuelStopAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'price_per_gallon')
    list_filter = ('state',)

admin.site.register(FuelStop, FuelStopAdmin)
