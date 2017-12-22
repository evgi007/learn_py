import sqlite3

# https://www.youtube.com/watch?v=pd-0G0MigUA&t=161s
conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute(""" CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer
#             )""")

conn.commit()

conn.close()