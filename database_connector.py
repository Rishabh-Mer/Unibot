import mysql.connector
import os

def getDb():
	return mysql.connector.connect(
        host = os.getenv('DATABASE_HOST'),
        user = os.getenv('DATABASE_USER'),
        password = os.getenv('DATABASE_PASSWORD'),
        database = os.getenv('DATABASE'),
        use_pure=True
	)

def executeQuery(query, parameters):
    myDb = getDb()
    mycursor = myDb.cursor()
    mycursor.execute(query, parameters)
    myDb.commit()


def DataUpdate(name, stream, semester):
	query = """INSERT INTO id_card_table ( name, stream, semester) VALUES (%s,%s,%s);"""
	executeQuery(query, (name, stream, semester))


def UserDataUpdate(name, phone, email):
	query = """INSERT INTO user_data (name, phone, email) VALUES (%s,%s,%s);"""
	executeQuery(query, (name, phone, email))


def UserMessage(message,response,sender):
	query = """INSERT INTO user_message (message, response, sender) VALUES (%s,%s,%s);"""
	executeQuery(query, (message, response, sender))

def StoreOtp(mobileNumber, otp):
	query = """INSERT INTO otp_mapping (mobile_number, otp) VALUES (%s,%s);"""
	executeQuery(query, (mobileNumber, otp))


def IsOtpValid(mobileNumber, otp):
	query = """SELECT * from otp_mapping where mobile_number = %s AND otp = %s limit 1"""
	myDb = getDb()
	mycursor = myDb.cursor(buffered=True)
	mycursor.execute(query, (mobileNumber, otp))
	return len(mycursor.fetchall()) == 1


def DeleteOtp(mobileNumber):
	query = """DELETE from otp_mapping where mobile_number = %s"""
	executeQuery(query, (mobileNumber,))

if __name__=="__main__":
	DataUpdate("bhavin", "Information Technology", "B.E")
