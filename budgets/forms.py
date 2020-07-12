from django.forms import ModelForm

from .models import Budget


class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = (
            'quantity', 'spending'
        )
