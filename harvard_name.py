# Lecture 6: (File I/O)
names = [] # 'list' - is a data structure that allows us to store multiple values into a single variable. 
for _ in range(3):
    names.append(input("What your name? "))
    #name = input("Whats your name? ")
    #names.append(name) #'append' -  method is used to add the name to our names list.
for name in sorted(names): #'sorted(names)' - creates a new list of names in alphabetical order.
    print(f"hello, {name}")