from myapp.models import IllustrationTag
from rest_framework import serializers


class IllustrationTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = IllustrationTag
        fields = '__all__'
