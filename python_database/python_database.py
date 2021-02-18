# first import the mysql connector

import mysql.connector

# import the error from mysql connector

from mysql.connector import Error


# define the connector function
def connect_fetch():
    '''function to connect and fetch rows in a database'''

    # create a variable for the connector object
    conn = None

    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='cape_codd',
            user='Mansa',
            password='@udubilly89',
            auth_plugin='mysql_native_password')
        # what to display once connection is successful
        print("Connected to Database")

        # select query
        sql_select_query = "select * from buyer"
        # cursor variable
        cursor = conn.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()

        # print select output
        print("\nPrinting each buyer record ")

        for rows in records:
            print("Buyer name: ", rows[0])
            print("Department: ", rows[1])
            print("Position: ", rows[2])
            print("Supervisor: ", rows[3])

    except Error as e:
        print('Not connecting due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Database shutdown!!')


if __name__ == '__main__':
    connect_fetch()
