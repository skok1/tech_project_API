from .models import Task, Category
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        # fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at', 'end_at', 'category']
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    # def create(self, validated_data):
    #     return Task.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.completed = validated_data.get('completed', instance.completed)
    #     instance.created_at = validated_data.get('created_at', instance.created_at)
    #     instance.updated_at = validated_data.get('updated_at', instance.updated_at)
    #     instance.end_at = validated_data.get('end_at', instance.end_at)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.save()
    #     return instance
