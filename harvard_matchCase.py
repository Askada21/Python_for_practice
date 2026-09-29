# Lecture 1: (Conditionals)
# Match Case is the same as in C language Switch Case
name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron": # In Match Case we use '|' instead of 'or'. We use it only here! Don't use in conditions!
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:  # the symbol '_' means the same as 'else' in conditions.
        print("Who?")

#if name == "Harry" or name == "Hermione" or name == "Ron":
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who?")
