from django.contrib import admin


class OwnerAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Owner model.
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'location', 'profile_image', 'resume')
    exclude = ('password', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'groups', 'user_permissions')
    search_fields = ('username', 'email', 'first_name', 'last_name')
