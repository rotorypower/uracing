from django.contrib import admin

from trackday.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "created_at")
    fields = ("author", "title", "image", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "text")
