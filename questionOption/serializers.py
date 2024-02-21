"""Serializer for user module"""

from rest_framework import serializers

from questionOption.models import QuestionOptionsForFemalesModel, QuestionOptionsForMalesModel


class AddNewQuestionOptionsForFemaleSerializer(serializers.ModelSerializer):
    """Serializer for adding new option for a question to ask to female"""
    question_id = serializers.IntegerField(default=None)
    titles = serializers.ListField(child=serializers.CharField(default=None))
    class Meta:
        """Meta class to change behaviour of model fields"""

        model = QuestionOptionsForFemalesModel
        fields = ['question_id','titles']  # Exclude all fields

class AddNewQuestionOptionsForMaleSerializer(serializers.ModelSerializer):
    """Serializer for adding new option for a question to ask to male"""
    question_id = serializers.IntegerField(default=None)
    titles = serializers.ListField(child=serializers.CharField(default=None))
    class Meta:
        """Meta class to change behaviour of model fields"""

        model = QuestionOptionsForMalesModel
        fields = ['question_id','titles']  # Exclude all fields
