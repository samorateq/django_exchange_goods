from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'image', 'category', 'condition']
        labels = {
            'title': 'Название товара',
            'description': 'Описание товара',
            'image': 'Фото товара',
            'category': 'Категория товара',
            'condition': 'Состояние товара',
        }
