from django.contrib import admin


class RepositoryImageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the RepositoryImage model.
    """
    search_fields = ['repository']
