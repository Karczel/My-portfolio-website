from django.contrib import admin


class RepositoryImageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the RepositoryImage model.
    """
    list_display = ['repository', 'image']
    search_fields = ['repository']
