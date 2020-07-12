from django.shortcuts import render
from django.views.generic import ListView

from .models import Budget
from .forms import BudgetForm


class BudgetListView(ListView):
    template_name = 'budgets/budget.html'
    queryset = Budget.objects.all().order_by('-pk')
