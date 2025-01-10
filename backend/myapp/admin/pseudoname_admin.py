from django.contrib import admin


class PseudoNameAdmin(admin.ModelAdmin):
    """
    Admin configuration for the PseudoName model.
    """
    search_fields = ['name']
