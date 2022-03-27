from django.contrib import admin

from topdriver.models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("axle_drive", "driver_name", "driver_car", "time", "created_at")
    fields = ("axle_drive", "driver_name", "driver_car", "time", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("axle_drive", "time")