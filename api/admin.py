from django.contrib import admin

from .models import CoffeeOrder, CoffeeProduct


@admin.register(CoffeeProduct)
class CoffeeProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "origin",
        "roast_level",
        "price",
        "intensity",
        "is_featured",
        "is_available",
    )
    list_filter = ("roast_level", "is_featured", "is_available")
    search_fields = ("name", "origin", "tagline")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(CoffeeOrder)
class CoffeeOrderAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "coffee",
        "quantity",
        "status",
        "phone_number",
        "created_at",
    )
    list_filter = ("status", "grind_size", "created_at")
    search_fields = ("customer_name", "phone_number", "address")
    autocomplete_fields = ("coffee",)
