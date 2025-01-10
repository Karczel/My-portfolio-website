from django.contrib import admin


class TagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Tag model.
    """
    search_fields = ['content']
