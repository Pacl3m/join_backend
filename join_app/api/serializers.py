from rest_framework import serializers
from join_app.models import Card, Category, Contact
from django.contrib.auth.models import User


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['color', 'name', 'value']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):

    firstName = serializers.CharField(write_only=True)
    lastName = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'firstName', 'lastName',
                  'email', 'password1']

    def save(self, **kwargs):
        email = self.validated_data['email']
        pw = self.validated_data['password1']

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'error': 'Email already exists'})

        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['firstName'],
            last_name=self.validated_data['lastName']
        )
        account.set_password(pw)
        account.save()
        return account
