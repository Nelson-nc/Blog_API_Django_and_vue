from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'password', 'profile_pic', 'bio']
        extra_kwargs = {'id': {"read_only": True},'password': {'write_only': True}}

    def create(self, validated_data):
        profile = Profile.objects.create_user(**validated_data)
        return profile