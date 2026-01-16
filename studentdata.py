"""
This file creates fake data for student records."""

import random, csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import base64
import io


# Professors: Takis (CS231, CS230), Eni (CS299, CS234), Carolyn (CS111, CS333)
# file 1: 40 students with distinct profiles (simulate student accounts)
# file 2: grades from three professors' courses

students = []
for i in range(1, 41):
        # all three Ps are random integers from 0 to 10
        pace = random.randint(0, 10)
        procrastination = random.randint(0, 10)
        prior_experience = random.randint(0, 10)
        email = random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + str(random.randint(100, 200)) + "@wellesley.edu"
        students.append({'student_id': i, 'email': email, 'pace': pace, 'procrastination': procrastination, 'prior_experience': prior_experience})

"""
# write to csv
with open('students.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['student_id', 'email', 'pace', 'procrastination', 'prior_experience'])
    for i in range(1, 41):
        # all three Ps are random integers from 0 to 10
        pace = random.randint(0, 10)
        procrastination = random.randint(0, 10)
        prior_experience = random.randint(0, 10)
        email = random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + str(random.randint(100, 200)) + "@wellesley.edu"
        writer.writerow({'student_id': i, 'email': email, 'pace': pace, 'procrastination': procrastination, 'prior_experience': prior_experience})
"""

course_professors = {
        'Panagiotis Metaxas': ['CS231', 'CS230'],
        'Eni Mustafaraj': ['CS299', 'CS234'],
        'Carolyn Anderson': ['CS111', 'CS333']
    }
grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "P", "F"]
for prof, courselst in course_professors.items():
    student_records = []
    for course in courselst:
        student_samp = random.sample(students, 15)
    for student in student_samp:
        grade = random.choice(grades)
        student_records.append({'student_id': student['student_id'], 'course': course, 'grade': grade, 'pace': student['pace'], 'procrastination': student['procrastination'], 'prior_experience': student['prior_experience']})
    with open(f'{prof}_grades.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['student_id', 'course', 'grade', 'pace', 'procrastination', 'prior_experience'])
        writer.writeheader()
        for record in student_records:
            writer.writerow(record)
