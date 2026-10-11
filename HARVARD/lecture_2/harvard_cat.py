# Lecture 2: (Loops)
# While Loop
# i = 0
# while i < 3:
#    print("meow")
#    i += 1

# For Loop
# for _ in range(3): # In Python, if such a variable does not have any other significance in our code, we can simply represent this variable as a single underscore '_'.
#    print("meow")

# print("meow\n" * 3, end="") # The \n creates a line break at the end of each meow, while end="" tells the interpreter not to add an extra line break after the final one.

# Task1
# while True:
#    n = int(input("What is n? "))
#    if n > 0:
#        break
# for _ in range(n):
#    print("meow")


def main():
    meow(get_number()) # сначала выполняется результат в get_number() и потом переходит в meow() с значением тоже самое что и meow(n).


def get_number(): #Она не принимает никаких аргументов, поэтому скобки пустые. Она сама спрашивает число и возвращает его.
    while True:
        n = int(input("What is n? "))
        if n > 0:
            return n # 'return' возвращает значение туда, откуда была вызвана функция. meow(get_number()) -> стало meow(3)


def meow(n): # А вот meow нужно число. Она ожидает, что при вызове ей дадут значение для n.
    for _ in range(n):
        print("meow")


main()
