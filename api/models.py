from django.db import models
from datetime import timedelta
from django.utils import timezone
import secrets


class APIKey(models.Model):
    key = models.CharField(max_length=100, unique=True, default=secrets.token_urlsafe)
    user=models.CharField(max_length=30, default=None)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"APIKey {self.key[:10]}... ({'Active' if self.active else 'Inactive'})"
    
class TokenUsage(models.Model):
    api_key = models.ForeignKey(APIKey, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    input_tokens = models.IntegerField(default=0)
    output_tokens = models.IntegerField(default=0)

    @classmethod
    def get_total_tokens(cls, date=timezone.now().date()):
        """ Get total input and output tokens used across all API keys for a given day """

        total = cls.objects.filter(timestamp__date=date).aggregate(
            total_input=models.Sum('input_tokens'),
            total_output=models.Sum('output_tokens')
        )
        return total['total_input'] or 0, total['total_output'] or 0

    @classmethod
    def get_total_input_tokens_today(cls):
        today = timezone.now().date()
        return cls.objects.filter(timestamp__date=today).aggregate(models.Sum('input_tokens'))['input_tokens__sum'] or 0
    
    @classmethod
    def get_total_output_tokens_today(cls):
        today = timezone.now().date()
        return cls.objects.filter(timestamp__date=today).aggregate(models.Sum('output_tokens'))['output_tokens__sum'] or 0


    def __str__(self):
        return f"Usage for {self.api_key.key[:10]} on {self.timestamp}"
    
