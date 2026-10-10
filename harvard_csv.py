# Lecture 6: (File I/O, CSV)
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",") # rstrip() - removes whitespace (spaces, tabs, and newline characters) from the end of a string.
        print(f"{row[0]} is in {row[1]}")