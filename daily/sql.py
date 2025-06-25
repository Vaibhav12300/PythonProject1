import sqlite3
conn=sqlite3.connect("db1.db")
conn.execute('''
create table users(
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_name VARCHAR(100),
pass VARCHAR(50)


)
''')
conn.close()