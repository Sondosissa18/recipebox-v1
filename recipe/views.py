from django.shortcuts import render

from recipe.models import Author, Recipe


def index(request):
    return render(
        request,
        "index.html",
        {"recipes": Recipe.objects.all(), "authors": Author.objects.all()},
    )


def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.get(id=recipe_id)
    return render(request, "recipe_detail.html", {"recipe": my_recipe})


def author_detail(request, author_id):
    my_author = Author.objects.get(id=author_id)
    return render(request, "author_detail.html", {"author": my_author})
