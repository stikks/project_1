import sqlite3

with sqlite3.connect("test.db") as connection:
	c = connection.cursor()
	#c.execute("""DROP TABLE quizzes""")
	c.execute("""CREATE TABLE quizzes(name TEXT, about TEXT)""")
	c.execute('INSERT INTO quizzes VALUES("star struck","about star stuff")')
	c.execute('INSERT INTO quizzes VALUES("star chucked","about stuff")')
