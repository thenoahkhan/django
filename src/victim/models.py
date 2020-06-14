from django.db import models

class Victim(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)
    desc = models.TextField(blank = False, null = False)
    date = models.DateField(blank = False, null = False)
    age = models.PositiveSmallIntegerField(blank = False, null = False)

