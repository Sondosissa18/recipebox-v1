from django.shortcuts import render, HttpResponseRedirect, reverse

from recipe.models import Author, Recipe
from recipe.forms import AddAuthorForm, AddRecipeForm


def index(request):
    return render(
        request,
        "index.html",
        {"recipes": Recipe.objects.all(), "authors": Author.objects.all()},
    )


def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.get(id=recipe_id)
    return render(request, "recipe_detail.html", {"recipe": my_recipe})


def add_author(request):
    html = "generic_form.html"
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_author = Author.objects.create(
                name=data["name"],
                bio=data["bio"],
            )
            return HttpResponseRedirect(
                reverse("homepage")
                # reverse("author_detail", kwargs={"author_id": new_author.id})
            )

    form = AddAuthorForm()
    return render(request, html, {"form": form})


def add_recipe(request):
    html = "generic_form.html"
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_recipe = Recipe.objects.create(
                title=data["title"],
                author=data["author"],
                description=data["description"],
                timerequired=data["timerequired"],
            )
            return HttpResponseRedirect(
                reverse("homepage")
                # reverse("recipe_detail", kwargs={"recipe_id": new_recipe.id})
            )
    form = AddRecipeForm()
    return render(request, html, {"form": form})


def author_detail(request, author_id):
    my_author = Author.objects.get(id=author_id)
    return render(request, "author_detail.html", {"author": my_author})
