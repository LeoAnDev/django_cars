"""
cars/admin.py
"""
from django.contrib import admin

from cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "model", "brand", "plate", "factory_year",
                    "model_year", "value", "status", "created_at", "updated_at")
    list_display_links = ("model",)
    list_editable = ("status",)
    search_fields = ("model", "brand", "plate", "factory_year",
                     "model_year", "value", "status")
    list_per_page = 5
