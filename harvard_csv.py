# Lecture 6: (File I/O, CSV)
students = []
with open("students.csv") as file:
    for line in file:
        #row = line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]}")
        name, house = line.rstrip().split(",") # rstrip() - removes whitespace (spaces, tabs, and newline characters) from the end of a string.
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)