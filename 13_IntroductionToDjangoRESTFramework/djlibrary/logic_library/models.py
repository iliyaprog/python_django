from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.name} {self.surname}"


class BookModel(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date_of_release = models.PositiveSmallIntegerField()
    isbn = models.DecimalField(max_digits=13, decimal_places=0)
    count_list = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name}"




