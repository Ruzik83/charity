from rest_framework import serializers
from .models import HelpRequest, Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'file']

class HelpRequestSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = HelpRequest
        fields = ['id', 'name', 'phone', 'description', 'created_at', 'media']

