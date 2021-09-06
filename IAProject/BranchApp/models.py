from django.db import models
from DeptApp.models import Dept

# Create your models here.
class Branch(models.Model):
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    intake = models.IntegerField()
    college_fees = models.FloatField(default=0)
    exam_fees = models.FloatField(default=0)



    def __str__(self) -> str:
        return f"{self.name}"
