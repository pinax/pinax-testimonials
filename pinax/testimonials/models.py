from django.db import models
from django.utils import timezone


class Testimonial(models.Model):

    text = models.TextField()
    author = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100, blank=True)
    added = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
