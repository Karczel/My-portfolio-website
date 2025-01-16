from django.contrib import admin


class PseudoNameAdmin(admin.ModelAdmin):
    """
    Admin configuration for the PseudoName model.
    """
    list_display = ['name']
    search_fields = ['name']
