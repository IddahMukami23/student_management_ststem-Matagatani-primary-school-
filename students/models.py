from django.db import models


# Create your models here.
class Student(models.Model):
    assessment_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    student_class = models.CharField(max_length=20)
    upi = models.CharField(max_length=20, unique=True)
    birth_certificate_number = models.CharField(max_length=20, unique=True)
    parent_name = models.CharField(max_length=100)

    def __str__(self):
        return f'Student: {self.name} {self.assessment_number} {self.upi}'
