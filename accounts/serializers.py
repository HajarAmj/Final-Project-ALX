from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username','email','password','first_name','last_name','date_of_birth')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email',''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name',''),
            last_name=validated_data.get('last_name',''),
            date_of_birth=validated_data.get('date_of_birth')
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','date_of_birth','profile_photo')
        read_only_fields = ('id','username','email')
