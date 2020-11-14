from django.shortcuts import render, HttpResponseRedirect, reverse, Http404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from recipe.models import Author, Recipe
from recipe.forms import AddAuthorForm, AddRecipeForm, LoginForm
from django.contrib.auth.views import LogoutView

from django.contrib.admin.views.decorators import staff_member_required


def index(request):
    return render(
        request,
        "index.html",
        {"recipes": Recipe.objects.all(), "authors": Author.objects.all()},
    )


@login_required()
def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.get(id=recipe_id)
    return render(request, "recipe_detail.html", {"recipe": my_recipe})


@login_required()
@staff_member_required()
def add_author(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if not request.user.is_staff:
        raise Http404("You do not have access to this page")

    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data["username"], password=data["password"]
            )
            Author.objects.create(name=data["name"], bio=data["bio"], user=new_user)
            return HttpResponseRedirect(reverse("homepage"))

    html = "generic_form.html"
    form = AddAuthorForm()
    return render(request, html, {"form": form})


@login_required()
def add_recipe(request):
    html = "generic_form.html"
    if request.user.is_staff:
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
                return HttpResponseRedirect(reverse("homepage"))
    else:
        if request.method == "POST":
            form = AddRecipeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_recipe = Recipe.objects.create(
                    title=data["title"],
                    author=Author.objects.get(user=request.user),
                    description=data["description"],
                    timerequired=data["timerequired"],
                )
                return HttpResponseRedirect(reverse("homepage"))

    form = AddRecipeForm()
    return render(request, html, {"form": form})


@login_required()
def author_detail(request, author_id):
    my_author = Author.objects.get(id=author_id)
    return render(request, "author_detail.html", {"author": my_author})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})
