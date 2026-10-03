# Lecture 4: (Libraries/Slice)
import sys # 'sys' - is a built-in Python module that lets your program interact with the system.
if len(sys.argv) < 2: # 'sys.argv' - gets arguments from the command line.
    sys.exit("Too few arguments") # 'sys.exit' - stops the program.

for arg in sys.argv:
    print("hello, my name is", arg)