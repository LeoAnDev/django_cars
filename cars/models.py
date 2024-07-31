"""
cars/models.py
"""

from uuid import uuid4

from django.db import models

from app import settings
from brands.models import Brand


class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    model = models.CharField(max_length=200, blank=False, null=False)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")
    factory_year = models.PositiveIntegerField()
    model_year = models.PositiveIntegerField()
    plate = models.CharField(max_length=20, blank=True, null=True)
    value = models.FloatField()
    photo = models.ImageField(upload_to="photo_cars/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, blank=False, null=False, choices=settings.STATUS_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.model} - {self.factory_year}"


class CarInventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cars_value = models.FloatField(null=True)
    cars_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.cars_count} - {self.cars_value}"
