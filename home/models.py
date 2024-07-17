from django.db import models

# Create your models here.
Approved_Dpt = [
    ('APH', 'Animal Science'),
    ('CSC', 'Computer Science'),
    ('MTH', 'Mathematics'),
]
class student(models.Model):
    name = models.CharField(max_length=255)
    reg_number = models.CharField(max_length=20, unique=True)
    dpt = models.CharField(max_length=30, choices=Approved_Dpt, default=Approved_Dpt[0][0])
    age = models.PositiveBigIntegerField(null=True, blank=True)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.name} - {self.reg_number}'