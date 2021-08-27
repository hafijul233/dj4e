import sqlite3

connection = None

try:
	connection = sqlite3.connect('email.sqlite')
	cursor = connection.cursor()
except Error as e:
	print(e)

finally:
	# Create new Table in DB
	# cursor.execute('DROP TABLE IF EXISTS counts;')
	cursor.execute('CREATE TABLE IF NOT EXISTS counts (email TEXT DEFAULT NULL, count INTEGER DEFAULT 0);')

	# receive email address from user
	email = input('Please enter a email address: ');
	if(len(email) >1):
		
		#check if email already exists
		cursor.execute('''SELECT * FROM counts WHERE email= ?;''', [email])
		row = cursor.fetchone()
		
		if row is None:
			cursor.execute('''INSERT INTO counts(email, count) VALUES(?, 1);''', [email])
			connection.commit()
			print("New Insert Successful. Row ID: "+str(cursor.lastrowid))
		else:
			cursor.execute('''UPDATE counts SET count = count+1 WHERE email = ?;''', [email])
			connection.commit()
			print("Row Count Updated. Row ID: "+str(cursor.lastrowid))
		