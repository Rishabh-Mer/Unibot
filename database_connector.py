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

def executeQuery(query):
    myDb = getDb()
    mycursor = myDb.cursor()
    mycursor.execute(query)
    myDb.commit()


def DataUpdate(name, stream, semester):
	query = 'INSERT INTO id_card_table ( name, stream, semester) VALUES ("{0}","{1}","{2}");'.format(name, stream, semester)
	executeQuery(query)


def UserDataUpdate(name, phone, email):
	query = 'INSERT INTO user_data (name, phone, email) VALUES ("{0}","{1}","{2}");'.format(name, phone, email)
	executeQuery(query)


def UserMessage(message,response,sender):
	query = 'INSERT INTO user_message (message, response, sender) VALUES ("{0}","{1}","{2}");'.format(message, response, sender)
	executeQuery(query)


def StoreOtp(mobileNumber, otp):
	query = 'INSERT INTO otp_mapping (mobile_number, otp) VALUES ("{0}","{1}");'.format(mobileNumber, otp)
	executeQuery(query)


def IsOtpValid(mobileNumber, otp):
	query = 'SELECT * from otp_mapping where mobile_number = "{0}" AND otp = "{1}" limit 1'.format(mobileNumber, otp)
	myDb = getDb()
	mycursor = myDb.cursor(buffered=True)
	mycursor.execute(query)
	return len(mycursor.fetchall()) == 1


def DeleteOtp(mobileNumber):
	query = 'DELETE from otp_mapping where mobile_number = "{0}"'.format(mobileNumber)
	executeQuery(query)

if __name__=="__main__":
	DataUpdate("bhavin", "Information Technology", "B.E")
