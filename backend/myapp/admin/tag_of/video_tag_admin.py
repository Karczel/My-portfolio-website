from django.contrib import admin


class VideoTagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the VideoTag model.
    """
    search_fields = ['name']
