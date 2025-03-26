from django.contrib.messages.context_processors import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from django.conf import settings
from .models import APIKey, TokenUsage
from .services import send_to_openai
from .serializers import ChatCompletionSerializer
import json
import tiktoken

MAX_TOKENS_PER_DAY = settings.DAILY_TOKEN_LIMIT  # Define max token usage limit


def count_tokens(messages):
    encoding = tiktoken.encoding_for_model("gpt-4")
    return len(encoding.encode(str(messages)))

class OpenAIRequestView(APIView):
    """API endpoint to process OpenAI requests and track token usage"""

    def post(self, request):
        api_key_value = request.headers.get('Authorization')
        if not api_key_value:
            return Response({'error': 'API key required'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            api_key = APIKey.objects.get(key=api_key_value, active=True)
            # print(api_key_value)
        except APIKey.DoesNotExist:
            return Response({'error': 'Invalid or inactive API key'}, status=status.HTTP_403_FORBIDDEN)

        messages = request.data.get('messages', '')
        if not messages:
            return Response({'error': 'Prompt is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Get total token usage for today
        total_input, total_output = TokenUsage.get_total_tokens()
        total_used = total_input + total_output

        # Enforce token limit
        if total_used+count_tokens(messages) >= MAX_TOKENS_PER_DAY:
            return Response({'error': 'Daily token limit exceeded'}, status=status.HTTP_429_TOO_MANY_REQUESTS)

        # Send request to OpenAI
        response, input_tokens, output_tokens = send_to_openai(api_key, messages)
        return Response({
            'response': ChatCompletionSerializer(response).data,
            'input_tokens': input_tokens,
            'output_tokens': output_tokens
        })
