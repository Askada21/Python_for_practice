# Lecture 2: (Loop)
#def main():
#    print_column(3)
#def print_column(height):
#    for _ in range(height):
#        print("#")
#main()

#def main():
#    print_row(4)
#def print_row(width):
#    print("?" * width)
#main()

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()

