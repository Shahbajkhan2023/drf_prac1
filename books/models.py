from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.IntegerField()
    cover_image = models.URLField(blank=True)
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.title
