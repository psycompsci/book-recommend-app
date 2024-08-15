import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import NearestNeighbors
# using cosine similarity for measuring similarity between books => use of NearestNeighbors

# Read the data and instantiate object to represent the data
#ratings = pd.read_csv('Ratings.csv')
#users = pd.read_csv('Users.csv')
books = pd.read_csv('books_shelf.csv')

# Drop duplicates and missing values
#ratings.drop_duplicates(inplace=True)
#ratings.dropna(inplace=True)
#users.drop_duplicates(inplace=True)
#users.dropna(inplace=True)
books.drop_duplicates(inplace=True)
books.dropna(inplace=True)

# extract genres columns
genres = books['genres']
# instantiate OneHotEncoder object
encoder = OneHotEncoder() 
# fit and transform genres column
genres_encoded = encoder.fit_transform(genres.values.reshape(-1, 1))

# instantiate NearestNeighbors object
recommender = NearestNeighbors(metric='cosine')

# get genres to recommender
recommender.fit(genres_encoded.toarray())

# Getting the recommendations
num_recommendations = 10
while(True):
    print("-----------------------------")
    print("Enter book ID: ")
    book_id = int(input())
    try:
        _, recommendations = recommender.kneighbors(genres_encoded[book_id].toarray(), n_neighbors=num_recommendations)

        
        # Extracting the book titles from the recommendations
        recommended_book_titles = books.iloc[recommendations[0]]['title']

        print("Recommended Books:")
        print(recommended_book_titles)

    except IndexError:
        print("Book ID not found.")

# can't find books after book id 9179 and -9180