from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at", "updated_at", "is_active")
    list_filter = ("created_at", "updated_at", "is_active")
    search_fields = ("name", "slug")
