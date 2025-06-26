from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Question(models.Model):
    Question = models.CharField(max_length=255, primary_key=True)
    Answer = models.TextField()
