import csv
from .models import Book

#path = '/Users/sheng/micropythonapi/bestsellers-with-categories.csv'
#path = 'https://github.com/ShenghaoHuang/micropythonapi/blob/main/bestsellers-with-categories.csv'
path = 'bestsellers-with-categories.csv'
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
