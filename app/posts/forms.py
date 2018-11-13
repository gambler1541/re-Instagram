from django import forms

class PostCreateForm(forms.Form):
    photo = forms.ImageField()