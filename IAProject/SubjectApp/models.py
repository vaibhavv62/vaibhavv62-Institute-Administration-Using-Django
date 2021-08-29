from django.db import models
from BranchApp.models import Branch

# Create your models here.
class Subject(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    def __str__(self) -> str:
        return f"{self.name}"