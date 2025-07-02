import os
import sys
import numpy as np



def list_students():
    students = [
        {"name": "철수", "score": 87},
        {"name": "영희", "score": 92},
        {"name": "민수", "score": 75}
    ]
    
    # avg = 0
    # sum =0
    # for student in students:
    #     sum += student["score"]
    #     avg = sum / len(students)
    # top = max(students, key=lambda x: x["score"])
    # for student in students:
    #     if (student["score"]>80):
    #         print(student["name"])
    sort = sorted(students, key=lambda x: x["score"], reverse=True)
    for student in sort:
        print({student["name"]: student["score"]})

list_students()