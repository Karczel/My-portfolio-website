from django.contrib import admin


class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Contact model.
    """
    list_display = ['platform', 'icon', 'link']
    search_fields = ['platform']

