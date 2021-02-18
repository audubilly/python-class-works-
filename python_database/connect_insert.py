import mysql.connector
from mysql.connector import Error


def connect_insert():
    ''' function to connect and insert a row in a database'''
    conn = None

    try:
        conn = mysql.connector.connect(host='localhost', database='firsttable', user='Mansa', password='@udubilly89')
        print('connecting to the database')

        if conn.is_connected:
            print('connected to database')
            db_cursor = conn.cursor()

            # create a variable to contain the sql query to be executed
            sql = "INSERT INTO human (Name, Colour, Gender,Bloodgroup,state) VALUES (%s,%s,%s,%s,%s)"

            # create a list of variable to contain all the values we want to insert into the database
            val = [
                ('Hannah', 'white', 'female', 'B-', 'lagos'),
                ('Micheal', 'Brown', 'Male', 'O-', 'lagos'),
                ('sandy', 'Black', 'Male', 'O+', 'lagos'),
                ('Green', 'Yellow', 'Male', 'AB', 'lagos'),
                ('Richard', 'Black', 'Male', 'B+', 'lagos')
            ]

        # execute the query using the execute many function
        db_cursor.executemany(sql, val)

        # commit to the database
        conn.commit()

        # print a success message
        print(db_cursor.rowcount, "rows was inserted.")

        # close the cursor
        db_cursor.close()

    except Error as e:
        print('connection failed due to the following:', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Disconnected from database')


if __name__ == '__main__':
    connect_insert()
