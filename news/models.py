from django.db import models
import datetime

class New(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    text = models.TextField()
    img = models.ImageField(upload_to='news/', null=True, blank=True)
    published = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f'"{self.title}" by {self.author}'