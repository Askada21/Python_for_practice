# Lecture 4: (Libraries/My Library)
import sys

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        goodbye(sys.argv[1])
    else:
        print("Usage: python harvard_myLibrary.py <name>")
