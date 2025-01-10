from django.contrib import admin


class IllustrationTagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the IllustrationTag model.
    """
    search_fields = ['illustration', 'tag']
