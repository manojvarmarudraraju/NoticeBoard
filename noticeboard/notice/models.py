from django.db import models

# Create your models here.

class Notice(models.Model):
    notice=models.CharField(max_length=1000)
    teachername = models.CharField(max_length=50)
    date = models.DateField()
    year = models.IntegerField()
    section = models.CharField(max_length=6)
    branch = models.CharField(max_length=10)
    def __str__(self):
        return self.notice
class FAQ(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    query=models.CharField(max_length=1000)
    def __str__(self):
        return self.query