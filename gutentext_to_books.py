#gutentext_to_books.py
# Program that converts a line-by-line .txt file from Gutenberg
#   into a list of books.
# Books will be scored and used as training data
#
#UCCS REU for Machine Learning in NLP 2019
#Brendan Bena - June 1st, 2019

import itertools
import gzip
import json
import pickle
import os


# Function that will create the necessary directory structure
def dir_constructor():
    
    if os.path.exists('pickles/') == False:
        os.mkdir('pickles/')
        

# Function to save a pickle of data
def pickle_list(alist, name):
        with open(path + name + '.pkl', 'wb+') as file:
                pickle.dump(alist, file, pickle.HIGHEST_PROTOCOL)


# Function that converts Allison Parrish's gutenberg corpus to a list of books
#  then pickles the booklist for later use
def guten_to_books():

    # Path to directories
    path = 'pickles/'

    # Create a list of lines from the gutenberg text
    lines = []
    for line in gzip.open('gutenberg-poetry-v001.ndjson.gz'):
        lines.append(json.loads(line.strip()))

    # Group poems on there 'GID' (unique number)
    #   essentially grouping by books
    poems_grouped = itertools.groupby(lines, key=lambda each: each['gid'])

    # List to hold strings of entire books
    book_list = []

    # Loop through each poem book by id
    #   pull string value from dictionary
    #       create string of entire book
    for gid, groups in poems_grouped:
        book_string = ''
        for group in groups:
            book_string += group['s'] + ' '
        book_list.append(book_string)

    return book_list


# Main Function
if __name__ == '__main__':

    # Path to directories
    path = 'pickles/'

    dir_constructor()
    print('Creating list of books')
    book_list = guten_to_books()
    # Save the pickle!!!
    pickle_list(book_list, 'booklist')
