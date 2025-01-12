from django.contrib import admin


class RepositoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Repository model.
    """
    list_display = ['name', 'link', 'product']
    search_fields = ['name']
