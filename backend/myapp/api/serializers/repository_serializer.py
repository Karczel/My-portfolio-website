from myapp.models import Repository
from rest_framework import serializers


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'
