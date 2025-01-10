from django.contrib import admin


class VideoAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Video model.
    """
    search_fields = ['name']
