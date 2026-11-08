import sqlite3
#conn = sqlite3.connect(':memory:') # :memory: - create a connection to a database in memory.

# connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

# update records
c.execute("""update customers set name = 'Bob' where surname = 'Elder'
        
    """)
conn.commit()

# create a table
c.execute("""create table if not exists customers (
        name text,
        surname text,
        email text
    )""")

# Data Types:
# NULL - does not exist
# INTEGER - numbers(whole: 1, 10, etc)
# REAL - decimal(10.5)
# TEXT - text
# BLOB - like images, music files

# many_customers = [
#                     ('Wes', 'Brown', 'wes@gmail.com'), 
#                     ('Steph', 'Kuewa', 'kuw@gmail.com'), 
#                     ('Dan', 'Pas', 'dan@gmail.com'),         
#                 ]

# c.executemany("insert into customers values(?,?,?)", many_customers)
#c.execute("insert into customers values('John', 'Elder', 'john@codemy.com')")

# query the database
c.execute("select rowid, * from customers")
# c.fetchone()
# c.fetchmany(3)
# print(c.fetchall()[0])
 
items = c.fetchall()

# print("NAME" + "\t\tEMAIL")
# print("----" + "\t\t--------")
# for item in items:
#     print(item[0] + " " + item[1] + " \t\t " + item[2])

#print("Command executed succesfully!")
# commit our command
conn.commit() # save 

# close our connection
conn.close()