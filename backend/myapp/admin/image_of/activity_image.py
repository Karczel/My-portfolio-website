from django.contrib import admin


class ActivityImageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ActivityTag model.
    """
    search_fields = ['activity']
