import sqlite3
#conn = sqlite3.connect(':memory:') # :memory: - create a connection to a database in memory.

# connect to database
# conn = sqlite3.connect('customer.db')

#create a cursor
# c = conn.cursor()

# update records
# c.execute("""update customers set name = 'Bob' where surname = 'Elder'
        
#     """)
# conn.commit()

# create a table
# c.execute("""create table if not exists customers (
#         name text,
#         surname text,
#         email text
#     )""")

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

#Query the DB and return all records
def show_all():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("select * from customers")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit() # save 

    conn.close()

# Add a new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("insert into customers values (?,?,?)", (first, last, email))
    conn.commit()
    conn.close()

# Add many records to table 
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("insert into customers values (?,?,?)", (list))
    conn.commit()
    conn.close()


# delete record from table
def delet_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("delete from customers where rowid = (?)", id)
    conn.commit()
    conn.close()

# Lookup with Where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("select * from customers where rowid = (?)", (email,))
    items = c.fetchall()
    
    for item in items:
        print(item)
        
    conn.commit()
    conn.close()
# query the database
# c.execute("select * from customers")
# c.fetchone()
# c.fetchmany(3)
# print(c.fetchall()[0])
 
# items = c.fetchall()

# for item in items:
#     print(item)

# print("NAME" + "\t\tEMAIL")
# print("----" + "\t\t--------")
# for item in items:
#     print(item[0] + " " + item[1] + " \t\t " + item[2])

#print("Command executed succesfully!")
# commit our command
# conn.commit() # save 

# close our connection
# conn.close()