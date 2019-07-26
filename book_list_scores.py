#book_list_scores.py
# Program that attempts to pull a list of book scores
#  then zip the scores to their proper Book ID
#  returns a pickle with the list of books and scores
#
#UCCS REU for Machine Learning in NLP 2019
#Brendan Bena - July 3rd, 2019

import itertools
import gzip
import json
import pickle

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

# Unpickle list of books and scores
book_list = unpickle_list('booklist')
book_scores = unpickle_list('bookscores')


# Initialize counters for each emotion
#  count number of books in each type of emotion category
#
# Create a list for the scores
#
#
joy = 0
trust = 0
anger = 0
sadness = 0
anticipation = 0
disgust = 0
fear = 0
surprise = 0

score_list = []

for book in book_scores:
    score_list.append(book[0])
    if book[0] == 'joy':
        joy += 1
    if book[0] == 'trust':
        trust += 1
    if book[0] == 'sadness':
        sadness += 1
    if book[0] == 'anticipation':
        anticipation += 1
    if book[0] == 'surprise':
        surprise += 1
    if book[0] == 'fear':
        fear += 1
    if book[0] == 'disgust':
        disgust += 1
    if book[0] == 'anger':
        anger += 1


# Number of books for each category
print('joy =', joy)
print('anger =', anger)
print('disgust =', disgust)
print('anticipation =', anticipation)
print('sadness =', sadness)
print('surprise =', surprise)
print('fear = ', fear)
print('trust = ', trust)


# Create a list of lines from the gutenberg text
lines = []
for line in gzip.open('guten_text/gutenberg-poetry-v001.ndjson.gz'):
    lines.append(json.loads(line.strip()))

# Group poems on there 'GID' (unique number)
#   essentially grouping by books
poems_grouped = itertools.groupby(lines, key=lambda each: each['gid'])

gid_list = []

for gid, groups in poems_grouped:
    gid_list.append(gid)

# Create final list 
gid_score_list = list(zip(gid_list, score_list))

# Save the pickle!
pickle_list(gid_score_list, 'gidscorelist')
