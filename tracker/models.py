from django.db import models
from django.core.urlresolvers import reverse



# Create your models here.

class Todo(models.Model):
    description = models.CharField(max_length=200)
    status = models.IntegerField()
    deadline = models.DateField()
    assignee = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('tracker:index')

    def __str__(self):
        return self.description


