from django.db import models
# from DeptApp.models import Dept
from BranchApp.models import Branch

# Create your models here.
class Prof(models.Model):
    # dept = models.ManyToManyField(Dept)
    branch = models.ManyToManyField(Branch)
    name = models.CharField(max_length=32)
    salary = models.FloatField()

    def __str__(self) -> str:
        return f"{self.name},{self.salary}"

    ret = ""
    def get_branch_values(self):
        print("Fetching branches...")
        global ret
        print("self.branch.all():-",self.branch.all())
        for branch in self.branch.all():
            print('Hello',branch.name)
            print(f"self.ret-{self.ret}")
            self.ret = self.ret + branch.name + ","
            print(self.ret[::])
        return self.ret