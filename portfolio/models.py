from django.db import models
from django.utils import timezone


class ExpenseItem(models.Model):
    description = models.CharField(max_length=144)
    amount = models.FloatField(null=True)
    published_at = models.DateTimeField(default=timezone.now)

