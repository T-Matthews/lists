
from django.db import models
from django.utils import timezone
import datetime
 
 
class Todo(models.Model):
    title = models.CharField(max_length=100,name='Title')
    details = models.TextField(verbose_name='Additional Notes')
    date = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return self.title