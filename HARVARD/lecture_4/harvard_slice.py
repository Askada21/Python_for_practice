# Lecture 4: (Libraries/Slice)
import sys # 'sys' - is a built-in Python module that lets your program interact with the system.
if len(sys.argv) < 2: # 'sys.argv' - gets arguments from the command line.
    sys.exit("Too few arguments") # 'sys.exit' - stops the program.

for arg in sys.argv[1:]: # '[1:]' - tell the interpreter to start at 1 and go to the end.
    print("hello, my name is", arg)