import sqlite3

db_file = 'Schedules.sqlite'
version_query = "SELECT sqlite_version();"
create_table_query = """
CREATE TABLE Schedules (
    docNumber INTEGER PRIMARY KEY,
    invoiceSet BOOLEAN,
    phoneNumber TEXT
);
"""


def connect_and_query_db(db_file, query, data=None):
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Database connected and successfully connected to SQLite")
        if data is not None:
            cursor.execute(query, data)  # Execute the query with data
        else:
            cursor.execute(query)  # Execute the query without data
        sqliteConnection.commit()  # Commit the transaction
        cursor.close()
        sqliteConnection.close()
        print("The SQLite connection is closed")
        return "Query executed successfully"
    except sqlite3.Error as error:
        print("Error while connecting to SQLite:", error)
        return None


# connect_and_query_db(db_file , create_table_query) 
# To Create the DB and Table 