from django.contrib import admin


class ActivityAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Activity model.
    """
    list_display = ['name', 'start_date', 'end_date', 'location', 'role']
    search_fields = ['name']

