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

def addFakeStudents(n):
    for _ in range(n):
        branch = random.choice(branches_list)
        rn = faker.random_int(0,1000)
        name = faker.name()
        marks = faker.random_int(0,100)
        college_fees = 20000 + rn
        exam_fees = 5000 + rn
        print("Branch-random.choice(branches_list):-",branch)
        print("RN-faker.random_int(0,1000):-",rn)
        print("Name-faker.name():-",name)
        print("Marks-faker.random_int(0,100):-",marks)
        print("college_fees:-",college_fees)
        print("exam_fees:-",exam_fees)

        stu = Student.objects.get_or_create(branch=branch,rn=rn,name=name,marks=marks,college_fees=college_fees,exam_fees=exam_fees)
        print("Student Record Added")

if __name__ == '__main__':
    n = int(input("How many student records do you want to add?"))
    addFakeStudents(n)