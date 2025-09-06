# 1

import sqlite3
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
cursor.execute(""" create table roster(name text, species text, age integer)""")
conn.close

# 2
import sqlite3
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
cursor.execute(""" insert into Roster values(('Benjamin Sisko', 'Human', 40),('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29))""")
conn.close

# 3


with.sqlite3.connect('my_database.db') as my_connection
    my_cursor = my_connection.cursor()
    query_str = "update roster where name = 'Jadzia Dax' set name = ' Ezri Dax' "
    resultat=my_cursor.execute(query_str)
    r1=resultat.fetchall()
    print(r1)



# 4

with sqlite3.connect("my_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute(""" select name age from roster where species = 'Bajoran'""")
    results = cursor.fetchall()
    for row in results:
    print(f"Name: {row[0]}, Age: {row[1]}")
