import sqlite3
conn = sqlite3.connect('database1.db')

print('Database connected.')

cmd = 'CREATE TABLE reservations (fname TEXT, lname TEXT, checkin TEXT, checkout TEXT, roomtype TEXT)'
conn.execute(cmd)

print('Table was created successfully.')

conn.close()