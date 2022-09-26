import sqlite3 as sql

with sql.connect('myDB.db') as con:
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
	data = [("Harry Potter", 1778, 3), ("Lord of the rings", 541, 5), ("Peppa the pig", 6, 123123)]
	cur.executemany("""
			INSERT INTO movie VALUES (?, ?, ?)
									
		""", data)
	res = cur.execute("""
			SELECT * FROM movie
		""")
	#con.commit()
	print(res.fetchall())