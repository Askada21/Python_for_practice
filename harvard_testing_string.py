# Lecture 5: (Testing String)
def main():
    name = input("Whats your name? ")
    hello(name)

def hello(to="world"):
    print("hello, ", to)

if __name__ == "__main__":
    main()