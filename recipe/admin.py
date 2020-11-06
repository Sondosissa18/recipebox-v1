from django.contrib import admin

# Register your models here.

from recipe.models import Author, Recipe


admin.site.register(Author)
admin.site.register(Recipe)