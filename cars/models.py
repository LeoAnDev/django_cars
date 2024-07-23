from uuid import uuid4
from django.db import models


class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    model = models.CharField(max_length=200)
    ano = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.model} - {self.ano}"
