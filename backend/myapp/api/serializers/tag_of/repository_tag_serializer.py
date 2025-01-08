from myapp.models import RepositoryTag
from rest_framework import serializers


class RepositoryTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryTag
        fields = '__all__'
