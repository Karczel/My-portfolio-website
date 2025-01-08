from myapp.models import Owner
from rest_framework import serializers


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'quote', 'about_me', 'location',
                  'profile_image', 'resume', 'requirements']

