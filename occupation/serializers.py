"""Serializer for designation module"""
from rest_framework import serializers

from occupation.models import OccupationModel


class AddOccupationModelSerializer(serializers.ModelSerializer):
    """Serializer for adding occupations"""

    class Meta:
        """Meta class to change behaviour of model fields"""
        model = OccupationModel
        exclude = ["created_at","updated_at"]


class GetAllOccupationSerializer(serializers.ModelSerializer):
    """Serializer for getting all occupations"""
    id = serializers.IntegerField(default=None)

    class Meta:
        """Meta class to change behaviour of model fields"""
        model = OccupationModel
        fields = ["id"]