from django.contrib import admin


class OwnerAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Owner model.
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'quote', 'about_me', 'location', 'profile_image',
                    'resume', 'requirements')
