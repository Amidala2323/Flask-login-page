import mysql.connector
from mysql.connector import connect, cursor
def Create_table():
    conn = mysql.connector.connect(user="root",
                                host="localhost",
                                database="mysite_database")
    cursorObject = conn.cursor()
    Table = """CREATE TABLE accoutns
                                (
                                    Name VARCHAR(255),
                                    Family VARCHAR(255),
                                    Email VARCHAR(255),
                                    Id VARCHAR(255),
                                    Username VARCHAR(255),
                                    password VARCHAR(255)
                                );"""
    cursorObject.execute(Table)



    print("Created")
def insert_data():
    conn = mysql.connector.connect(user="root",
                                host="localhost",
                                database="mysite_database")

    cursorObject = conn.cursor()

    data = "INSERT INTO test (Name, password) VALUES (%s, %s)"
    data2 = "INSERT INTO accoutns (Name, Family, Email, Id, Username, password) VALUES (%s, %s, %s, %s, %s, %s)"
    val = ("Mohammad", "Khandan", "alirezakhandan313@gmail.com", "2345", "parziball", "password@password")
    cursorObject.execute(data2, val)
    conn.commit()
    print("Entered Data")
    conn.close()
def select_data():
    conn = mysql.connector.connect(user="root",
                                host="localhost",
                                database="flask_app")

    cursorObject = conn.cursor()

    query = "SELECT Name, password FROM test"

    cursorObject.execute(query)
    result = cursorObject.fetchall()

    for x in result:

        print(type(x))
        print(x[1])

    conn.close()

insert_data()