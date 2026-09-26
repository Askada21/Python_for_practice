# We can move our function down but if we do it. We need to have a main() func start(up).
def main():
    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()

# Create our own function
def hello(to="world"):
    print("hello,", to)

# Restore our program
main()