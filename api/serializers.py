from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    """Serializer for the message part of a choice."""
    role = serializers.CharField()
    content = serializers.CharField()

class ChoiceSerializer(serializers.Serializer):
    """Serializer for a choice in the OpenAI chat completion response."""
    index = serializers.IntegerField()
    message = MessageSerializer()
    finish_reason = serializers.CharField()

class UsageSerializer(serializers.Serializer):
    """Serializer for the usage object of the OpenAI response."""
    prompt_tokens = serializers.IntegerField()
    completion_tokens = serializers.IntegerField()
    total_tokens = serializers.IntegerField()

class ChatCompletionSerializer(serializers.Serializer):
    """Serializer for the entire chat completion response."""
    id = serializers.CharField()
    object = serializers.CharField()
    created = serializers.IntegerField()  # Timestamp for when the response was created
    model = serializers.CharField()
    choices = ChoiceSerializer(many=True)  # A list of choices
    usage = UsageSerializer()  # Usage information
