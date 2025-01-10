from django.contrib import admin


class RepositoryTagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the RepositoryTag model.
    """
    search_fields = ['repository', 'tag']
