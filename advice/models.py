from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    time_remaining = models.IntegerField(help_text="Time remaining to complete the course in months")

    def __str__(self):
        return self.name
