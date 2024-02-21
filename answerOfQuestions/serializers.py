"""Serializer for user module"""

from rest_framework import serializers

from answerOfQuestions.models import AnswersOfFemalesModel, AnswersOfMalesModel


class AddAnswersOfFemaleSerializer(serializers.ModelSerializer):
    """Serializer for adding new answer of female"""
    user_id = serializers.IntegerField()
    answers = serializers.ListField(child=serializers.CharField())
    class Meta:
        """Meta class to change behaviour of model fields"""

        model = AnswersOfFemalesModel
        fields = ["user_id","answers"]

class AddAnswersOfMaleSerializer(serializers.ModelSerializer):
    """Serializer for adding new answer of male"""
    user_id = serializers.IntegerField()
    answers = serializers.ListField(child=serializers.CharField())
    class Meta:
        """Meta class to change behaviour of model fields"""

        model = AnswersOfMalesModel
        fields = ["user_id","answers"]