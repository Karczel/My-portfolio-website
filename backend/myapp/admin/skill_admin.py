from django.contrib import admin


class SkillAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Skill model.
    """
    search_fields = ['skill', 'type']

