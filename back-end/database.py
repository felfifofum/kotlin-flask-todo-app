import sqlite3

conn = sqlite3.connect('todolist.db')

c = conn.cursor()

things_todo = [
                ('take pet out for a walk'),
                ('clean my room'),
                ('organise my bookself'),
                ('buy bread, milk and fish')
            ]

#c.execute("""CREATE TABLE todolist (
#        todo_item text
#    )""")

c.execute("INSERT INTO todolist VALUES ('wash dirty laundy'),('take pet out for a walk')")
c.execute("SELECT * FROM todolist")
print(c.fetchone()[0])


conn.commit()

conn.close()