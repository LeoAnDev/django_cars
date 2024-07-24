from django.contrib import admin

from brands.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status", "created_at", "updated_at")
    list_display_links = ("name",)
    list_editable = ("status",)
    search_fields = ("name", "status")
    list_per_page = 5
