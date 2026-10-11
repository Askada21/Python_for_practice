# Lecture 7: (Regular Expressions)
# Regular expressions (regex) are patterns used to find, check, or replace text.
email = input("What is your email? ").strip()
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")