from django import forms

from .models import Post


class PostForm(forms.Form):
    """ модель формы 3 поля. label - человекочитаемая подпись на форме"""
    title = forms.CharField(max_length=200, label='x')
    data1 = forms.CharField(max_length=200, label='y')
    data2 = forms.CharField(max_length=200, label='z')
    class Meta:

        fields = ('title', 'data1', 'data2')
