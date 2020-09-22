import mysql.connector
from mysql.connector import errorcode
import os

def migrate():
    myDb = mysql.connector.connect(host=os.getenv('DATABASE_HOST'),user=os.getenv('DATABASE_USER'),password=os.getenv('DATABASE_PASSWORD'),database=os.getenv('DATABASE'),use_pure=True)

    cursor = myDb.cursor()

    TABLES = {}
    TABLES['user_data'] = \
        'create table `user_data`( `name` varchar(40) null, `email` varchar(40) null, `phone` varchar(15) null) ENGINE=InnoDB'
    TABLES['id_card_table'] = \
        'create table `id_card_table`( `name` varchar(40) null, `stream` varchar(40) null, `semester` varchar(40) null ) ENGINE=InnoDB'
    TABLES['user_message'] = \
        'create table `user_message`( `message` varchar(1024) null, `response` varchar(1024) null, `sender` varchar(100) null ) ENGINE=InnoDB COLLATE = utf8mb4_unicode_ci'
    TABLES['opt_mapping'] = \
        'create table `otp_mapping`( `mobile_number` varchar(40) null, `otp` varchar(40) null ) ENGINE=InnoDB'

    print(TABLES)
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print ('Creating table {0}', table_name)
            cursor.execute(table_description)
        except (mysql.connector.Error, err):
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('already exists.')
            else:
                print(err.msg)
        else:
            print('OK')

    cursor.close()
    myDb.close()

migrate()

