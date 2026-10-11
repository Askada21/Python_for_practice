# Lecture 2: (List)
students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)

print()

# Length 
for i in range(len(students)): # len() показывает количество элементов в списке (3).
    # Здесь i используется как индекс, чтобы получить студента из списка: students[0]  -> "Hermione" etc
    print(i + 1, students[i]) # i + 1 -> номер для человека. students[i] -> получить элемент списка.

print()

# Dictionaries - are a data structure that allows you to associate keys with values.
#students = {
    # KEY          VALUE
#    "Hermione": "Gryffindor",
#    "Harry": "Gryffindor",
#    "Ron": "Gryffindor",
#    "Draco": "Slytherin",
#}
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
] # [ ]  → list (список). { }  → dictionary (словарь)
for student in students:
    #print(student, students[student], sep=", ") # sep=", " - separate 
    print(student["name"], student["house"], student["patronus"], sep=", ")
