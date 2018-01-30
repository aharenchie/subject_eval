from django.db import models

class Question(models.Model):
    question_id = models.IntegerField(default=0)
