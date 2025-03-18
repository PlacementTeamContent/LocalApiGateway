from openai import OpenAI
from django.conf import settings
from .models import TokenUsage
from datetime import date
from django.utils.timezone import now
import datetime

# OpenAI API Key (Set this in settings.py)
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def send_to_openai(api_key, messages):
    """ Send prompt to OpenAI and return the response while tracking token usage """

    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    # print(prompt)
    # print(response)

    # Get token counts
    input_tokens = response.usage.prompt_tokens
    output_tokens = response.usage.completion_tokens

    # Update token usage for today
    token_record, created = TokenUsage.objects.get_or_create(api_key=api_key, timestamp=now())
    token_record.input_tokens += input_tokens
    token_record.output_tokens += output_tokens
    token_record.save()

    return response, input_tokens, output_tokens
