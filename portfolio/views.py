from django.shortcuts import render
from .models import ExpenseItem

def index(request):
    context = {
        "title": "Portfolio"
    }
    return render(request, 'portfolio/home_page.html', context)


def about(request):
    return render(request, 'portfolio/about.html', context = {})


def expenses_home(request):
    current_expenses = ExpenseItem.objects.all()
    context = {
        "title":"Current Expenses",
        "expenses":current_expenses
    }

    return render(request, 'portfolio/expenses_home.html', context)