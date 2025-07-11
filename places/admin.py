from django.contrib import admin

from .models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "user", "rating")
    list_filter = ("category", "user")
    search_fields = ("name", "description")
