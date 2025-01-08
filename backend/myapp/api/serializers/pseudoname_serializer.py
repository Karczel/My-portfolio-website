from myapp.models import PseudoName
from rest_framework import serializers


class PseudoNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PseudoName
        fields = '__all__'
