from myapp.models import Illustration
from rest_framework import serializers


class IllustrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illustration
        fields = '__all__'
