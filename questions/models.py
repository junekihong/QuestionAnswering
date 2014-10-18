from django.db import models
from django.utils import timezone
import datetime

class AudioQuestion(models.Model):
    user_id = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id

class TextQuestion(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)
    question_healthcenter_id = models.CharField(max_length=200, default=" ")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(TextQuestion)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    choice_healthcenter_id = models.CharField(max_length=200, default=" ")

    def __str__(self):
        return self.choice_text
