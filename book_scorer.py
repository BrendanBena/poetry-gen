#book_scorer.py
# Program that will attempt to score books/poems based on their emotion score
#     returning the emotion score and keeping track of the top score and
#     returning tuple values of book GID and top emotion score
#     Books will then be written to text files based on the emotion scores
#     For training data.
#
#UCCS REU for Machine Learning in NLP 2019
#Brendan Bena - July 2nd, 2019

import pickle
from score_sentence import scored_sentence, get_score
import re

# Path for files
path = 'pickles/'

# Function to save a pickle file
def pickle_list(alist, name):
        with open(path + name + '.pkl', 'wb+') as file:
                pickle.dump(alist, file, pickle.HIGHEST_PROTOCOL)

# Function to pull pickle file
def unpickle_list(name):
    with open(path + name + '.pkl', 'rb') as file:
        return pickle.load(file)

# Create list of books from booklist pickle
book_list = unpickle_list('booklist')

# Create emolex dictionary from pickle file
dict_list = unpickle_list('dictlist')

# Create index for progression reasons
book_index = 0

# Holds scores for all the books 
book_scores = []

# Loop through all books in list 
for book in book_list:
    # Increment
    book_index += 1
    # Create scoring class out of books
    scored_book = scored_sentence(book)
    print('Splitting Book #', book_index)
    # Splits entire book by words -- using a RegEx to take care of commas and apostrophes
    re_book = re.findall(r'\w+|\S+', scored_book)
    print('Book # ', book_index, ' split')
    # Look through entire book for emotion words
    for token in re_book:
        # Score potential emotion words
        #   add emotion scores to book score
        emotion_word_scores = get_score(dict_list, token)
        scored_book.add_score(emotion_word_scores)
    print('Book Score for Book # ', book_index)
    book_score = scored_book.return_max_score()
    print()
    book_scores.append(book_score)

# Save the pickle!!!
pickle_list(book_scores, 'bookscores')
    
