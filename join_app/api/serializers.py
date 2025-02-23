from rest_framework import serializers
from join_app.models import Card, Category, Contact

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        # fields = ['assignedUser', 'assignedUserFullName', 'category', 'description', 
        #           'dueDate', 'listType', 'prio', 'progress', 'subtasks', 'title']
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['color', 'name', 'value']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
