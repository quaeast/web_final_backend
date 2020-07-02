from django.db import models


class Student(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    schoolId = models.CharField(max_length=200)

    def __str__(self):
        return self.name
