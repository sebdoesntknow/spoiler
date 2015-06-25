from django.db import models

# Create your models here.

class Title(models.Model):
    title_text = models.CharField(max_length=100)
    sub_date = models.DateTimeField('Date Submitted')

class Spoiler(models.Model):
    title = models.ForeignKey(Title)
    spoiler_text = models.TextField()
    pub_date =  models.DateTimeField('Date Added')
    votes = models.IntegerField(default=0)
