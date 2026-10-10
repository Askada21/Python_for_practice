# Lecture 6: (File I/O, CSV)
import csv
name = input("What is your name? ")
home = input("What is your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictReader(file, fieldnames =["name", "home"])
    writer.writerow({"name": name, "home": home})