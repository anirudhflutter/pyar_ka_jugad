"""Serializer for user module"""

from rest_framework import serializers

from question.models import QuestionForFemaleModel, QuestionForMaleModel


class AddNewQuestionForFemaleSerializer(serializers.ModelSerializer):
    """Serializer for adding new question to ask to female"""

    class Meta:
        """Meta class to change behaviour of model fields"""

        model = QuestionForFemaleModel
        exclude = ["is_active","is_deleted","created_at", "updated_at"]

class AddNewQuestionForMalesSerializer(serializers.ModelSerializer):
    """Serializer for adding new question to ask to male"""

    class Meta:
        """Meta class to change behaviour of model fields"""

        model = QuestionForMaleModel
        exclude = ["is_active","is_deleted","created_at", "updated_at"]
