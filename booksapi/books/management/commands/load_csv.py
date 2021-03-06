import os.path
import csv
from ...models import Book
from django.core.management.base import BaseCommand

#BASE_DIR = os.path.dirname('micropythonapi')
#BASE_DIR = os.path.dirname(os.path.abspath('micropythonapi'))
#path = (BASE_DIR +'/booksapi/staticfiles/bestsellers-with-categories.csv')
# path = 'https://github.com/ShenghaoHuang/micropythonapi/blob/main/bestsellers-with-categories.csv'
# path = 'bestsellers-with-categories.csv'
class Command(BaseCommand):

    def handle(self, *args, **options):
        BASE_DIR = os.path.dirname(os.path.abspath('micropythonapi'))
        path = (BASE_DIR + '/booksapi/staticfiles/bestsellers-with-categories.csv')
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
