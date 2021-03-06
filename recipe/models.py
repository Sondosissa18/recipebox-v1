from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.bio}"


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    timerequired = models.CharField(max_length=100)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.author}"
