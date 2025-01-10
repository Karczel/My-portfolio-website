from django.contrib import admin


class ActivityAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Activity model.
    """
    search_fields = ['name']

