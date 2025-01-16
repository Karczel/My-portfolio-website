from myapp.models import SkillTag
from rest_framework import serializers


class SkillTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTag
        fields = '__all__'
