from rest_framework import serializers

from .models import User


class HelloSerializer(serializers.Serializer):
    """Serializes a name field"""
    name = serializers.CharField(max_length=10)


class UserSerializer(serializers.ModelSerializer):
    """Serializes a user object"""

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # Override default create function
    def create(self, validated_data):
        """Create and return new user"""
        user = User.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user
