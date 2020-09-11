import mysql.connector
import os

def DataUpdate(name, stream, semester):
	mydb = mysql.connector.connect(
        host = os.getenv('DATABASE_HOST'),
        user = os.getenv('DATABASE_USER'),
        password = os.getenv('DATABASE_PASSWORD'),
        database = os.getenv('DATABASE'),
        use_pure=True
	)

	mycursor = mydb.cursor()

	sql_query2 = 'INSERT INTO id_card_table ( name, stream, semester) VALUES ("{0}","{1}","{2}");'.format(name, stream, semester)

	mycursor.execute(sql_query2)

	mydb.commit()

	print(mycursor.rowcount, "id record inserted")

def UserDataUpdate(name, phone, email):
	mydb = mysql.connector.connect(
        host = os.getenv('DATABASE_HOST'),
        user = os.getenv('DATABASE_USER'),
        password = os.getenv('DATABASE_PASSWORD'),
        database = os.getenv('DATABASE'),
        use_pure=True
	)

	mycursor = mydb.cursor()

	sql_query1 = 'INSERT INTO user_data (name, phone, email) VALUES ("{0}","{1}","{2}");'.format(name, phone, email)

	mycursor.execute(sql_query1)

	mydb.commit()

	print(mycursor.rowcount, "user record inserted")

if __name__=="__main__":
	DataUpdate("bhavin", "Information Technology", "B.E")