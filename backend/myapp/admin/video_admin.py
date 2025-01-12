from django.contrib import admin


class VideoAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Video model.
    """
    list_display = ['name', 'link']
    search_fields = ['name']
