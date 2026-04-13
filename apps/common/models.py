from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    """Abstract base model with timestamp fields for all models."""
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True