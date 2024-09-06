from django.db import models

# Create your models here.
class LibraryBook(models.Model):
    title  = models.CharField(max_length=100)
    author  = models.CharField(max_length=150)
    isbn  = models.CharField(max_length=100, unique=True)
    available  = models.BooleanField(default=True)

    class Meta:
        ordering = ["author"]
        indexes = [models.Index(fields=["isbn"], name="isbn_idx"),]

    def __str__(self):
        return f"{self.title} by {self.author}"