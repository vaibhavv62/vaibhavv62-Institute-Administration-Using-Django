from django.db import models
# from DeptApp.models import Dept
from BranchApp.models import Branch

designation_choices = (
    ('Peon','Peon'),
    ('Lab Assistant','Lab Assistant'),
    ('Sweeper','Sweeper'),
    ('Librarian','Librarian'),
    ('Computer Operator','Computer Operator'),
    ('Clerk','Clerk'),
    ('Security Guard','Security Guard'),
)
# Create your models here.
class Staff(models.Model):
    # dept = models.ManyToManyField(Dept)
    branch = models.ManyToManyField(Branch)
    name = models.CharField(max_length=32)
    designation = models.CharField(max_length=32,choices=designation_choices)
    salary = models.FloatField()

    def __str__(self) -> str:
        return f"{self.name},{self.designation},{self.salary}"

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