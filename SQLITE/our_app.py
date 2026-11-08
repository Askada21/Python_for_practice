import sqlite_pract3

# add a resord to the database 
sqlite_pract3.add_one("Lara","Smit","lara@gmail.com")

# delete record use rowid as string
# sqlite_pract3.delet_one('6')

# Lookup email address record
sqlite_pract3.email_lookup("john@codemy.com")

# add many records 
# stuff = [
#     ('Brend', 'Smiter', 'br@gmail.com'),
#     ('Joshua', 'Pesos', 'jo@gmail.com')
#     ]
# sqlite_pract3.add_many(stuff)

# show all records
# sqlite_pract3.show_all()