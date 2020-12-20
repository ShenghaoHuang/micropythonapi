from django.db import models
import csv


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    rating = models.FloatField(default=0)
    reviews = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    year = models.CharField(max_length=8)
    genre = models.CharField(max_length=32)

    def __str__(self):
        return self.name


path = '/Users/sheng/micropythonapi/bestsellers-with-categories.csv'
with open(path) as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        _, created = Book.objects.get_or_create(
            name=row[0],
            author=row[1],
            rating=row[2],
            reviews=row[3],
            price=row[4],
            year=row[5],
            genre=row[6]
        )
