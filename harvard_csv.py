# Lecture 6: (File I/O, CSV)
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})
        #row = line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]}")
        #name, house = line.rstrip().split(",") # rstrip() - removes whitespace (spaces, tabs, and newline characters) from the end of a string.
        #student = {"name": name, "house": house}
        #students.append(student)
        #students.append(f"{name} is in {house}")

#def get_name(student):
#    return student["name"]

#for student in sorted(students):
for student in sorted(students, key=lambda student: student["name"]): # lambda - use when a function has no name.
    print(f"{student['name']} is in {student['house']}")
