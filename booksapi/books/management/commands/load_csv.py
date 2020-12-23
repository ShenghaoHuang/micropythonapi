import os
import csv
#from booksapi.books.models import Book
from ...models import Book

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, '/booksapi/staticfiles/bestsellers-with-categories.csv')
#path = 'https://github.com/ShenghaoHuang/micropythonapi/blob/main/bestsellers-with-categories.csv'
#path = 'bestsellers-with-categories.csv'
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