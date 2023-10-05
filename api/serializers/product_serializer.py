from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    id = serializers.CharField(max_length=8)
    title = serializers.CharField(max_length=8)
    