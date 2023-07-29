import mysql.connector
import pandas as pd

class MySQLConnection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def __enter__(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

# Set database connection parameters
HOST = ""
DATABASE = ""
USER = ""
PASSWORD = ""

# Create database connection using context manager
with MySQLConnection(HOST, DATABASE, USER, PASSWORD) as db_connection:
    # Create a cursor object
    cursor = db_connection.cursor()
    print("Connected to:", db_connection.get_server_info())

    # Read data from CSV file
    csv_file_path = r"path to csv file"
    csvreader = pd.read_csv(csv_file_path)

    csvreader['page_number'] = csvreader['page_number'].astype(int)

    # Handle missing values by converting them to None
    csvreader = csvreader.where(pd.notna(csvreader), None)

    # Insert data into MySQL table
    query = """INSERT INTO Summary (submission_number, date_obtained,page_number, text_embedded, text_ocr ) VALUES (%s,%s, %s, %s, %s )"""
    for ind in csvreader.index:
        tuple = (csvreader['submission_number'][ind],
                csvreader['date_obtained'][ind],
                int(csvreader['page_number'][ind]), 
                csvreader['text_embedded'][ind], 
                csvreader['text_ocr'][ind] )
        cursor.execute(query, tuple)
    db_connection.commit()
