import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import NearestNeighbors
# using cosine similarity for measuring similarity between books => use of NearestNeighbors

# Read the data and instantiate object to represent the data
#ratings = pd.read_csv('Ratings.csv')
#users = pd.read_csv('Users.csv')
books = pd.read_csv('Sample_new.csv')

# Drop duplicates and missing values
#ratings.drop_duplicates(inplace=True)
#ratings.dropna(inplace=True)
#users.drop_duplicates(inplace=True)
#users.dropna(inplace=True)
books.drop_duplicates(inplace=True)
books.dropna(inplace=True)

# extract authors columns
# first line of Books.csv: ISBN,Book-Title,Book-Author,Year-Of-Publication,Publisher,Image-URL-S,Image-URL-M,Image-URL-L
# first line of Ratings.csv: User-ID,ISBN,Book-Rating
# first line of Users.csv: User-ID,Location,Age
ratings = books['average_rating']
encoder = OneHotEncoder()
ratings_encoded = encoder.fit_transform(ratings.values.reshape(-1, 1))

# instantiate NearestNeighbors object
recommender = NearestNeighbors(metric='cosine')

# git authors to recommender
recommender.fit(ratings_encoded.toarray())

book_index = 0
num_recommendations = 3

# Getting the recommendations
_, recommendations = recommender.kneighbors(ratings_encoded[book_index].toarray(), n_neighbors=num_recommendations)

# Extracting the book titles from the recommendations
recommended_book_titles = books.iloc[recommendations[0]]['title']
