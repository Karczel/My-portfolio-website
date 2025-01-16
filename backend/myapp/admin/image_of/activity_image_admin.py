from django.contrib import admin


class ActivityImageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ActivityTag model.
    """
    list_display = ['activity', 'image']
    search_fields = ['activity']
