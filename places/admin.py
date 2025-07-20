from django.contrib import admin

from .models import Place


@admin.action(description="Mark selected places disabled")
def make_places_disabled(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="Mark selected places Enabled")
def make_places_enabled(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "user", "rating", "is_active")
    list_filter = ("category", "user", "is_active")
    search_fields = ("name", "description")
    actions = [make_places_disabled, make_places_enabled]
