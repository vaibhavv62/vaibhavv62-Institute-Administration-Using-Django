import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','IAProject.settings')

import django
django.setup()

import random
from faker import Faker
from BranchApp.models import Branch
from ProfApp.models import Prof
# from . import ProfApp


faker = Faker()
branches_list = Branch.objects.all()

n = int(input("How many professor records do you want to add?"))
for _ in range(n):
    br = random.choice(branches_list)
    name = faker.name()
    salary = faker.random_int(0,100)
    print("Branch-random.choice(branches_list):-",br)
    print("Name-faker.name():-",name)
    print("Marks-faker.random_int(0,100):-",salary)

    '''
    try:
        prof = Prof.objects.get_or_create(branch=branch,name=name,salary=salary)
    except Prof.DoesNotExist:
        prof = Prof(branch=branch,name=name,salary=salary)
        prof.save()
        print("Professor Record Added")
    '''
    prof = Prof(name=name,salary=salary)
    prof.save()
    prof.branch.add(br)
    print("Professor Record Added")
