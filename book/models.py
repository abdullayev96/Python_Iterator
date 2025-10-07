from django.db import models
from baseapp.models import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator




class Author(BaseModel):
    full_name = models.CharField(max_length=500, verbose_name="Author to'liq ismi")
    bio = models.TextField()
    photo = models.ImageField(upload_to="images/", verbose_name="Author ni rasmi")
    # book_number = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0),], verbose_name="Kitoblar soni ")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Muallif"



class Book(BaseModel):
    name = models.CharField(max_length=500, verbose_name="Kitobni nomi")
    description = models.TextField(verbose_name="Kitob haqida ")
    image = models.ImageField(upload_to='book/', blank=True, verbose_name="Kitobni rasmi")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Kitobning Muallifi", related_name="books")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kitoblar_"


