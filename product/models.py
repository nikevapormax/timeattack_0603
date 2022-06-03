from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        db_table = 'category'

    category = models.CharField(max_length=50)


class Drink(models.Model):
    class Meta:
        db_table = 'drink'

    drink = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)