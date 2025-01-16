from django.contrib import admin


class IllustrationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Illustration model.
    """
    list_display = ['image', 'name']
    search_fields = ['name']


