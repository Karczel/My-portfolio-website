from django.contrib import admin


class TagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Tag model.
    """
    list_display = ['content']
    search_fields = ['content']
