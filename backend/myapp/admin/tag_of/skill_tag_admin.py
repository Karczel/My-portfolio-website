from django.contrib import admin


class SkillTagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SkillTag model.
    """
    list_display = ['skill', 'tag', 'certificate']
    search_fields = ['skill', 'tag']
