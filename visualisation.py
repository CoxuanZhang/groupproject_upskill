"""
This file creates fake data for student records."""

import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from flask import Flask, render_template, send_file, jsonify
import base64
import io

grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "P", "F"]

def load_data(prof,select_grades,crit):
    # Load data from CSV files
    with open(f'{prof}_grades.csv', 'r') as f:
        reader = csv.DictReader(f)
        grade_records = [row for row in reader]
    print(grade_records[0])
    crit_values = [grade_record[crit] for grade_record in grade_records if grade_record['grade'] in select_grades]
    return crit_values

def visualise(prof, crit, lowest = 'P'):
    select_grades = grades[:grades.index(lowest)+1]
    crit_values = load_data(prof, select_grades, crit)
    if not crit_values:
        return "Unfortunately, there are no students matching the criteria. You can be the first!"
    crit_values = [int(value) for value in crit_values]
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
    ax.set_xlabel(f'Avergae {crit} for students of {prof} with grades above {select_grades[-1]}')
    ax.set_title('Heatmap with Average Line on Colorbar')

    plt.tight_layout()
    plt.legend()
    plt.show()

    #convert to base64 string
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', dpi=150)
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close(fig)
    return image_base64

#app = Flask(__name__)
if __name__ == "__main__":
    visualise('Panagiotis Metaxas', 'pace')