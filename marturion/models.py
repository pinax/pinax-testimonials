import datetime

from django.db import models



class Testimonial(models.Model):
    
    text = models.TextField()
    author = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100, blank=True)
    added = models.DateTimeField(default=datetime.datetime.now)
    active = models.BooleanField(default=False)
