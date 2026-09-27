# Lecture 1:
def main():
    x = int(input("What is x? "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")

# Pythonic
def is_even(n):
    return n % 2 == 0
#    return True if n % 2 == 0 else False

#def is_even(n):
#    if n % 2 == 0:
#        return True
#    else:
#        return False

main()


#if x % 2 == 0:
#       print("Even") # ЧЕТНЫЙ
#else:
#    print("Odd") # НЕЧЕТНЫЙ
