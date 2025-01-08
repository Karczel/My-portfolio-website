from myapp.models import ActivityImage
from rest_framework import serializers


class ActivityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityImage
        fields = '__all__'
