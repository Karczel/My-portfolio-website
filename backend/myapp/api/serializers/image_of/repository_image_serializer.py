from myapp.models import RepositoryImage
from rest_framework import serializers


class RepositoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryImage
        fields = '__all__'
