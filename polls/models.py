from django.db import models

# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('datetime published')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choice

