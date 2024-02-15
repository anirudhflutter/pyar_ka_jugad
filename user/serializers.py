from rest_framework import serializers
from user.models import UserModel

class FileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = UserModel.images.through
        fields = ('url',)

    def get_url(self, instance):
        return instance.file.url
    
class UserSignUpSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(default=None)
    last_name = serializers.CharField(default=None)
    phone_number = serializers.CharField(default=None)
    gender = serializers.CharField(default=None)
    birth_date = serializers.DateField(default=None)
    country_id = serializers.IntegerField(default=None)
    state_id = serializers.IntegerField(default=None)
    city_id = serializers.IntegerField(default=None)
    images = FileSerializer(many=True, read_only=True) 
    height = serializers.CharField(default=None)
    weight = serializers.CharField(default=None)
    instagram_id = serializers.CharField(default=None, allow_null=True)
    instagram_account_link = serializers.CharField(default=None, allow_null=True)
    designation = serializers.CharField(default=None)
    occupation = serializers.CharField(default=None)

    class Meta:
        model = UserModel
        exclude = [
            "is_free_trial_user",
            "is_verified",
            "is_active",
            "is_deleted",
            "created_at",
            "updated_at",
        ]

    def validate_country(self, value):
        if not value.pk:
            raise serializers.ValidationError("Invalid country id")
        return value

    def validate_state(self, value):
        if not value.pk:
            raise serializers.ValidationError("Invalid state id")
        return value

    def validate_city(self, value):
        if not value.pk:
            raise serializers.ValidationError("Invalid city id")
        return value