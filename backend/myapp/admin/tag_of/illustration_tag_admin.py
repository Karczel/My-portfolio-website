from django.contrib import admin


class IllustrationTagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the IllustrationTag model.
    """
    list_display = ['illustration', 'tag']
    search_fields = ['illustration', 'tag']
