from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.URLField(max_length = 50)
    body = models.CharField(max_length = 500)
    replies = models.IntegerField(default=0)

    def __str__(self): 
        return self.title

class Answer(models.Model):
    text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    def __str__(self): 
        return self.text

