# -*- coding: utf-8 -*-
"""movie recommendation system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kPFUaA-CPyDgZhN6Pim6wSmtuf--rAJ2
"""

#used for mathematical fucntions for arrays
import numpy as np

#useed to create dataframes a
import pandas as pd
#module that provides classes and funvtion for comparing sequence and generating the difference btn them
import difflib

# used to transform text document into numerical vectors which can then be used as input for machine learning algorithms
from sklearn.feature_extraction.text import TfidfVectorizer

#used to calculate the cosine similarity btn pairs of samples
from sklearn.metrics.pairwise import cosine_similarity

import csv
import pandas as pd

# Initialize an empty list to store the rows of the CSV file
rows = []

# Open the CSV file and read it line by line
with open('/content/movies.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    # Iterate over each row in the CSV file
    for row in reader:
        try:
            # Attempt to append the row to the list
            rows.append(row)
        except Exception as e:
            # If an error occurs, print the error and skip this row
            print("Error occurred:", e)
            continue

# Convert the list of rows into a pandas DataFrame
movies_data = pd.DataFrame(rows[1:], columns=rows[0])

# Now you have your DataFrame loaded with the data from the CSV file

# Print the first five rows of the DataFrame
movies_data.head()

# number of rows and columns in the data frame

movies_data.shape

# selecting the relevant features for recommendation since we have alot of columns, so we will choose the ones that will be relevant for this work

selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)

# now we will create a for loop to replace the null valuess with null string

for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')

  #we will the null values with a null string

#why we handle the null data
  # Consistency in Data Handling: By replacing null values with null strings across all selected features, you ensure consistency in how missing values are represented in your dataset. This consistency simplifies data processing and analysis because you're treating missing values uniforml

# combining all the 5 selected features

combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

print(combined_features)

# Replace NaN values with empty strings
combined_features = combined_features.fillna('')

# converting the text data to feature vectors/ numerical values

vectorizer = TfidfVectorizer()

#now we are coming to fit and transform the combined_features into numerical values and store it in the feature_vector
#we do vectorization because alot of what machine learning has to do with is massively numbers and vectors
feature_vectors = vectorizer.fit_transform(combined_features)

print(feature_vectors)

"""our data had looked differently when we used the combined
_feature but now that we've vectorized it, it now looks like numbers as seen above
"""

# getting the similarity scores using cosine similarity
#the cosine similarity is a metric used to measure the similarities btn two vectors
#so we will feed our feature_vector to the cosine similarity to get the similarities so we can know which movies are related
similarity = cosine_similarity(feature_vectors)

print(similarity)

print(similarity.shape)

# getting the movie name from the user

movie_name = input(' Enter your favourite movie name : ')

# creating a list with all the movie names given in the dataset

list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)

# finding the close match for the movie name given by the user
# we will use the difflib cause it contains a library called get_close_match

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)

close_match = find_close_match[0]
print(close_match)

# finding the index of the movie with title from the dataframe in a form of a list

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)

# getting a list of similar movies by getting the similarity score value with all the movies


# Convert index_of_the_movie to an integer
index_of_the_movie = int(index_of_the_movie)

# Get the length of the similarity list
num_movies = len(similarity)

# Make sure that the index_of_the_movie is a valid index
if index_of_the_movie >= num_movies or index_of_the_movie < 0:
    raise IndexError("Invalid index")

# Get the list of similar movies
similarity_score = list(enumerate(similarity[index_of_the_movie]))

# Print the similarity score
print(similarity_score)

"""so the first value is the movie index, and the next value is the score against the iron man movie

so the index 0 is the avatar and its similarity score with the iron man is the 0.021949576792612023

"""

#all movies checked against the ironman in the similarity score which is all the movies
len(similarity_score)

# sorting the movies based on their similarity score, the higher the similarity score, the more close it is to the ironmen
#so we use the reverse to arrange it in the descending order(reverse order)

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print(sorted_similar_movies)

"""(68, 1.0000000000000002) is where the lambda x:x[1] comes in. In the sense that its going to the index 1 in this case which would be the 1.00000000000000002 which is the similarity score to order and arrnage the results in the descendin order"""

# print the name of similar movies based on the index

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1

"""MOVIE RECOMMENDATION SYSTEM"""

#only putting th previous codes together as one
movie_name = input(' Enter your favourite movie name : ')

list_of_all_titles = movies_data['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

close_match = find_close_match[0]

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1

