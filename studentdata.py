"""
This file creates fake data for student records."""

import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from flask import Flask, render_template, send_file, jsonify
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
        'Takis': ['CS231', 'CS230'],
        'Eni': ['CS299', 'CS234'],
        'Carolyn': ['CS111', 'CS333']
    }
grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "P", "F"]
grade_records = []
for prof, courselst in course_professors.items():
    grade_records.append({'Professor': prof, 'Student': {}})
    for course in courselst:
        student_samp = random.sample(students, 15)
    for student in student_samp:
        grade = random.choice(grades)
        grade_records[-1]['Student']= {'student_id': student['student_id'], 'course': course, 'grade': grade}

def visualise(prof, crit, lowest = 'P'):
    select_grades = grades[:grades.index(lowest)+1]
    select_students = [grade_record['Student']['student_id'] for grade_record in grade_records if grade_record['Professor'] == prof and grade_record['Student']['grade'] in select_grades]
    if not select_students:
        return "Unfortunately, there are no students matching the criteria. You can be the first!"
    crit_values = [students[student_id - 1][crit] for student_id in select_students]
    avg = np.mean(crit_values)

    fig=plt.figure(figsize=(8,2))
    ax=fig.add_subplot(111)
    vals=[0,2,4,6,8,10]
    color = ['#F5CB5C',"#F5DE5C","#F5F55C","#C9E94B","#98DF6C"]
    color1 = ['#F5CB5C',"#E3F55C","#BDF55C","#5CF5CC","#5CDEF5","#5CAEF5"]
    color2 = ['#2c7bb6','#0a793a','#77a353','#f1d499','#c96a33','#975114']
    cmap = mpl.colors.ListedColormap(color)
    norm = mpl.colors.BoundaryNorm(vals, cmap.N)
    cb = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                norm=norm,
                                spacing='uniform',
                                orientation='horizontal',
                                extend='neither',
                                ticks=vals)
    cb.ax.axvline(x=avg, color='red', linewidth=3, linestyle='--', label=f'Average: {avg:.2f}')
    cb.ax.text(avg, 0.5, f'   Avg: {avg:.1f}', 
             va='center', ha='left', color='#242423', fontweight='bold')
    ax.set_xlabel(f'Avergae {crit} for students of {prof} with grades above {select_grades[-1]}')
    ax.set_title('Heatmap with Average Line on Colorbar')

    plt.tight_layout()

    #convert to base64 string
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', dpi=150)
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close(fig)
    return image_base64

app = Flask(__name__)
