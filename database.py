import mysql.connector

def connect_to_database():
    try:
        # Establish connection
        db_connection = mysql.connector.connect(
            host="localhost",
            user="phat",
            password="phat",
            database="taskDB"
        )
        print("Connected to the database")
        return db_connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None

def close_connection(db_connection):
    try:
        # Close connection
        db_connection.close()
        print("Connection to the database closed")
    except mysql.connector.Error as error:
        print("Error closing MySQL database connection:", error)
