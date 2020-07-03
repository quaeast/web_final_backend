from django.db import models


class Student(models.Model):
    owner = models.OneToOneField('auth.User', related_name='owner_Student', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='')
    schoolId = models.CharField(max_length=20, default='')
    gender = models.CharField(max_length=10, default='')
    birthday = models.CharField(max_length=50, default='')
    nation = models.CharField(max_length=10, default='')
    politicsStatus = models.CharField(max_length=20, default='')
    isArmy = models.CharField(max_length=20, default='')
    maritalStatus = models.CharField(max_length=20, default='')
    universityOfGraduation = models.CharField(max_length=50, default='')
    majorOfGraduation = models.CharField(max_length=50, default='')
    schoolOfGraduation = models.CharField(max_length=50, default='')
    UndergraduateYear = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=100, default='')
    zipCode = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=100, default='')
    cellPhone = models.CharField(max_length=100, default='')
    result = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name
