from django.contrib import admin

from .models import Favorite


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "place")
    list_filter = ("user",)
    search_fields = ("place__name",)
