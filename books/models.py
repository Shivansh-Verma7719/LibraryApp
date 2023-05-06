from django.db import models


class Book_md(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField(default=None)
    isbn = models.CharField(max_length=20)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
