import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    #Connect to class Question that tells Django that each Choice is related to a single Question, unlike sa traditional na database query which is specify ang ang primary key na field, sa Django kay naa na siyay built-in na default primary key
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):                      #add '__str__' method to model to return the string value of a specified field
        return self.choice_text
