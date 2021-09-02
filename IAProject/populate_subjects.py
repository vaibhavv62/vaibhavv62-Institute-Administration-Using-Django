import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','IAProject.settings')

import django
django.setup()

import random
from faker import Faker
from BranchApp.models import Branch
from SubjectApp.models import Subject


faker = Faker()
branches_list = Branch.objects.all()

n = int(input("How many subject records do you want to add?"))
for _ in range(n):
    branch = random.choice(branches_list)
    name = branch.name + 'subj' + str(faker.random_int(0,1000))
    print("Branch-random.choice(branches_list):-",branch)
    print("Branch Name-:-",name)

    stu = Subject.objects.get_or_create(branch=branch,name=name)
    print("Subject Record Added")