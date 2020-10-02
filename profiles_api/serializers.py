from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """this is to test our serializes"""
    name = serializers.CharField(max_length=10)

    
