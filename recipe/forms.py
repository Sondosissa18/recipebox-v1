# class Recipe(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     description = models.TextField()
#     timerequired = models.CharField(max_length=100)
#     instructions = models.TextField()

#     def __str__(self):
#         return f"{self.title} - {self.author}"


from django import forms

from recipe.models import Recipe, Author


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)

    timerequired = forms.CharField(max_length=50)
