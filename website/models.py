from django.db import models
from datetime import datetime
from django.utils import timezone
import pytz


class Contact(models.Model):
    name = models.CharField(max_length=200, help_text='Type name')
    phone = models.CharField(max_length=15, help_text='Type phone')
    email = models.EmailField(null=True, help_text='Type email')
    link = models.CharField(max_length=150, help_text='Type link')

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.title


class FeedbackForm(models.Model):
    author_message_name = models.CharField(max_length=128)
    author_message_email = models.EmailField()
    message_text = models.TextField()
    message_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.author_message_name
