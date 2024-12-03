"""
Definition of forms.
"""

from cProfile import label
from codecs import charmap_build
from dataclasses import fields
from email import message
from msilib.schema import Class
from random import choices
from tkinter import Widget
from traceback import format_exception
from xml.dom.minidom import Attr
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog



class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))


class feedbackForm(forms.Form):
        name = forms.CharField(label='Ваше имя', min_length=2, max_length=20)
        surname = forms.CharField(label='Ваша фамилия', min_length=2, max_length=20)
        gender = forms.ChoiceField(label='Ваш пол', choices=[('1', 'Женский'), ('2','Мужской')], widget=forms.RadioSelect, initial = 1)
        estimation = forms.ChoiceField(label='Оцените наш салон от 1 до 5', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], widget=forms.RadioSelect, initial =1)
        email = forms.EmailField(label='Ваша почта', min_length=8)
        notice = forms.BooleanField(label='Хотите получать рассылку на почту?', required=False)
        message = forms.CharField(label='Ваши предложения и замечания', widget=forms.Textarea(attrs={'rows':12, 'cols':20}))




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image')
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}