from django.db import models
from BranchApp.models import Branch

# Create your models here.
class Student(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    rn = models.IntegerField(unique=True)
    name = models.CharField(max_length=32)
    marks = models.FloatField()
    college_fees = models.FloatField(default=0)
    exam_fees = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"{self.rn},{self.name}"