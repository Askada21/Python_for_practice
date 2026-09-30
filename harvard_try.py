# Lecture 3: (Exceptions)
# You use try when some code might cause an error.
# "Try doing this; if it fails with an error, handle the error."
#while True:
#    try:
#        x = int(input("What's x?"))
#    except ValueError:
#        print("x is not an integer")
#    else:
#        break
#print(f"x is {x}")

def main():
    x = get_int("What is x ? ")
    print(f"x is {x}")

def get_int(prompt):

    while True:
        try:
            #x = int(input("What is x ? "))
            #print(f"x is {x}")
            #return int(input("What is x? "))
            return int(input(prompt))
        except ValueError:
            #print("x is not an integer")
            pass # Do nothing. "I know something happened, but I don't want to do anything about it here."
        #else:
            # also can use break
            #return x # Send 10 back to var called get_int
main()