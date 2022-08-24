from unittest.util import _MAX_LENGTH
from django import forms

class CreatorsForm(forms.Form):
    fullname = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField(max_length=150)

class LoginForm(forms.Form):
    email = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class SubjectForm(forms.Form):
    title = forms.CharField(max_length=150)
    writer = forms.CharField(max_length=100)
    price = forms.IntegerField()

class ChapterForm(forms.Form):
    chaptername = forms.CharField(max_length=150)
    pagenumber = forms.IntegerField()
    writername = forms.CharField(max_length=150)

class SubChapterForm(forms.Form):
    subchaptername = forms.CharField(max_length=150)
    writername = forms.CharField(max_length=150)
    pagenumber = forms.IntegerField()
