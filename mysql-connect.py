import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    host='localhost',
    user='sqluser',
    password='password',
    database='recommendation'
)

cursor = connection.cursor()

# Load CSV into DataFrame
df = pd.read_csv('Sample.csv')

# Insert DataFrame into MySQL
for index, row in df.iterrows():
    cursor.execute("INSERT INTO books (isbn, title, author, year, publisher, image_url_s, image_url_m, image_url_l) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", tuple(row))

connection.commit()
cursor.close()
connection.close()
