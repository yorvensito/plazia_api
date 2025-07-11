from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "place", "rating", "created_at")
    list_filter = ("rating", "user", "created_at")
    search_fields = ("place__name", "text")
