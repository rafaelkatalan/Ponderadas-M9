import sqlite3

conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()
c.execute('''SELECT * FROM sensor_data''')
print(c.fetchall())
conn.commit()
conn.close()