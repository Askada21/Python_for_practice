# Lecture 4: (Libraries/Packages)
# One of the reasons Python is so popular is that there are numerous powerful third-party 
# libraries that add functionality. We call these third-party libraries, implemented as a folder, “packages”.
# PyPI is a repository or directory of all third-party packages currently available.
import cowsay
import sys
if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])