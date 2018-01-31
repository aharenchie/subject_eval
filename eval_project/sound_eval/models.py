from django.db import models

class Question(models.Model):
    question_id = models.IntegerField(default=100)
    question_max = models.IntegerField(default=100)

class Time_data(models.Model):
    start_time = models.FloatField(default=100.00)
