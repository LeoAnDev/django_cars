"""
brands/models.py
"""

from uuid import uuid4

from django.db import models

from app import settings


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    status = models.CharField(
        max_length=20, blank=False, null=False, choices=settings.STATUS_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
