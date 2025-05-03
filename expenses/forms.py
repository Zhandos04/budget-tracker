from django import forms
from .models import Transaction, Category

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'date', 'category', 'transaction_type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.TextInput(attrs={'placeholder': 'Введите описание'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Введите сумму'}),
        }
        labels = {
            'amount': 'Сумма',
            'description': 'Описание',
            'date': 'Дата',
            'category': 'Категория',
            'transaction_type': 'Тип транзакции',
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите название категории'}),
        }
        labels = {
            'name': 'Название категории',
        }