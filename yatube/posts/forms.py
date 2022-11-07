from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group']

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
