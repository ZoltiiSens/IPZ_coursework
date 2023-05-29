from django.forms import ModelForm
from .models import Week, Todo


class todo_week_form(ModelForm):
    class Meta:
        model = Week
        fields = ['title',]


class todo_todo_form(ModelForm):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'md', 'td', 'wd', 'th', 'fr', 'st', 'sd']

