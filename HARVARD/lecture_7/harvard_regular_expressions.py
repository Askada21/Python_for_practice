# Lecture 7: (Regular Expressions)
# Regular expressions (regex) are patterns used to find, check, or replace text.
import re

email = input("What is your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
#username, domain = email.split("@")
