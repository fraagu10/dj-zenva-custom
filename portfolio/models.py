from django.db import models
from django.utils import timezone
from django.conf import settings


EXPENSE_TYPE_CHOICES = [
    ("Income", "Income"),
    ("Expense", "Expense"),
]


class ExpenseLog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    log_name = models.CharField(max_length=144, blank=True, null=True, verbose_name="Log Name")
    initial_budget = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    

    def __str__(self):
        return f'{self.log_name}'


class ExpenseItem(models.Model):
    description = models.CharField(max_length=144)
    amount = models.FloatField(blank=True, default=0)
    published_at = models.DateTimeField(default=timezone.now)
    expense_log = models.ForeignKey(ExpenseLog, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=54, choices=EXPENSE_TYPE_CHOICES, null=True)

    def __str__(self):
        return f'{self.type}: {self.description}'
    

