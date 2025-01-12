from django.contrib import admin


class RepositoryTagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the RepositoryTag model.
    """
    list_display = ['repository', 'tag']
    search_fields = ['repository', 'tag']
