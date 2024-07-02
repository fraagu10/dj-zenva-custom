from django.contrib import admin
from .models import ExpenseItem, ExpenseLog


admin.site.register(ExpenseItem)
admin.site.register(ExpenseLog)
