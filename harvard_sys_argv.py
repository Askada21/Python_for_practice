# Lecture 4: (Libraries/Statistics)
# MEAN/AVG
#import statistics
#print(statistics.mean([100, 90]))

# SYS/ARGV
#import sys # 'sys' - is a module that allows us to take arguments at the command line.
#try:
#    print("hello, my name is", sys.argv[1]) # argv is a list within the sys module that records what the user typed on the command line.
#except IndexError:
#    print("Too few argumemts")

import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
    
print("hello, my name is", sys.argv[1])