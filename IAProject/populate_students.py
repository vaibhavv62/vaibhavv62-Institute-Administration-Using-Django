import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','IAProject.settings')

import django
django.setup()

import random
from faker import Faker
from BranchApp.models import Branch
from StudentApp.models import Student


faker = Faker()
branches_list = Branch.objects.all()

n = int(input("How many student records do you want to add?"))
for _ in range(n):
    branch = random.choice(branches_list)
    rn = faker.random_int(0,1000)
    name = faker.name()
    marks = faker.random_int(0,100)
    print("Branch-random.choice(branches_list):-",branch)
    print("RN-faker.random_int(0,1000):-",rn)
    print("Name-faker.name():-",name)
    print("Marks-faker.random_int(0,100):-",marks)

    stu = Student.objects.get_or_create(branch=branch,rn=rn,name=name,marks=marks)
    print("Student Record Added")