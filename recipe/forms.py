from django import forms

from recipe.models import Recipe, Author


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=200)
    bio = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)

    timerequired = forms.CharField(max_length=50)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
