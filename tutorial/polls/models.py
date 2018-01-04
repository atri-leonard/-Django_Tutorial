import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
# A question model that entails text of question and publish date
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Return string representation of question
    def __str__(self):
        return self.question_text

    # Return if this method was created recently
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


# A choice model that entails text of choice, votes count and foreign key that links to a question
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Return string representation of choice
    def __str__(self):
        return self.choice_text
