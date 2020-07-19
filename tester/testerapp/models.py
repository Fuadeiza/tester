from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class testQuestions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    question= models.TextField()
    option1= models.TextField()
    option2= models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    answer= models.TextField()

    def __str__(self):
        return self.question
