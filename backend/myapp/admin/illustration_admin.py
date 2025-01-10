from django.contrib import admin


class IllustrationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Illustration model.
    """
    search_fields = ['name']


