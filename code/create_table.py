import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id int, username text,password text)"
cursor.execute(create_table)

connection.commit()

connection.close()
