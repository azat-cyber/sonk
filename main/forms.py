from .models import Task, Image
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),

            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
