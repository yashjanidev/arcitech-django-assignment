from rest_framework import serializers
from .models import User, Content


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    pincode = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name',
                  'phone', 'address', 'city', 'state', 'country', 'pincode']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            address=validated_data.get('address'),
            city=validated_data.get('city'),
            state=validated_data.get('state'),
            country=validated_data.get('country'),
            pincode=validated_data['pincode'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ContentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    title = serializers.CharField(required=True)
    body = serializers.CharField(required=True)
    summary = serializers.CharField(required=True)
    document = serializers.FileField(required=True)

    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'summary', 'document',
                  'categories', 'author', 'created_at', 'updated_at']
