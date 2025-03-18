from django.urls import path
from .views import OpenAIRequestView

app_name = 'api'

urlpatterns = [
    path('api/v1/openai/', OpenAIRequestView.as_view(), name='openai_request'),
]