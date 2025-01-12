from django.contrib import admin


class VideoTagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the VideoTag model.
    """
    list_display = ['video', 'tag']
    search_fields = ['video', 'tag']
