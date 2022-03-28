from django.contrib import admin

from racewars.models import FotoContent


@admin.register(FotoContent)
class FotoContentAdmin(admin.ModelAdmin):
    list_display = ("content", "image")
    fields = ("content", "image")
    search_fields = ("content",)
