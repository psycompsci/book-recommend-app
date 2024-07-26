import mysql.connector
import pandas as pd
from sklearn.impute import SimpleImputer

# Connect to MySQL
connection = mysql.connector.connect(
    host='localhost',
    user='sqluser',
    password='password',
    database='recommendation'
)

cursor = connection.cursor()

# Load CSV into DataFrame
df = pd.read_csv('books.csv', quotechar='"', encoding='utf-8')

# Separate numeric and non-numeric columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
non_numeric_cols = df.select_dtypes(exclude=['float64', 'int64']).columns

# Handle missing values (e.g., filling with mean)
imputer_numeric = SimpleImputer(strategy='mean')
df[numeric_cols] = imputer_numeric.fit_transform(df[numeric_cols])

# Handle missing values for non-numeric columns (e.g., filling with the most frequent value)
imputer_non_numeric = SimpleImputer(strategy='most_frequent')
df[non_numeric_cols] = imputer_non_numeric.fit_transform(df[non_numeric_cols])

# Insert DataFrame into MySQL
for index, row in df.iterrows():
    try:
        cursor.execute("INSERT INTO books (book_id, goodreads_book_id, best_book_id, work_id, books_count, isbn, authors, original_publication_year, title, language_code, average_rating, ratings_count, work_ratings_count, image_url, small_image_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row))
    except mysql.connector.errors.DataError as e:
        print(f"Error occurred at row {index + 1}: {e}")
        print(row)


connection.commit()
cursor.close()
connection.close()
