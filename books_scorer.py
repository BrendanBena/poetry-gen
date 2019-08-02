#books_scorer.py
# Program that scores an inputted list of (bookstring,id) tuples
#   then print the total number of poems/books in each category
#   as well as save the associated pickle files
#
#UCCS REU for Machine Learning in NLP 2019
#Brendan Bena - July 1st, 2019
import pickle
import re
import inspect
from operator import itemgetter


# Class to hold an emotion score for 
class scored_text(str):
    
    # Initialize with 0 for emotion scores
    def __init__(self, sentence):
        self.sentence = sentence
        self.anger = 0
        self.anticipation = 0
        self.joy = 0
        self.trust = 0
        self.fear = 0
        self.surprise = 0
        self.sadness = 0
        self.disgust = 0
        
    # Function that takes a dictionary of emotion scores and adds it to class score
    def add_score(self, emotion_dict):
        self.anger = self.anger + emotion_dict.get('anger', 0)
        self.anticipation = self.anticipation + emotion_dict.get('anticipation', 0)
        self.joy = self.joy + emotion_dict.get('joy', 0)
        self.trust = self.trust + emotion_dict.get('trust', 0)
        self.fear = self.fear + emotion_dict.get('anger', 0)
        self.surprise = self.surprise + emotion_dict.get('surprise', 0)
        self.sadness = self.sadness + emotion_dict.get('sadness', 0)
        self.disgust = self.disgust + emotion_dict.get('disgust', 0)
        
    # Function that attempts to return the max emotion score a sentence
    def return_max_score(self):
        score_list = []
        iterdict = iter(self.__dict__.items())
        next(iterdict)
        for attr, val in iterdict:
            score_list.append((attr, int(val)))
        print(max(score_list,key=itemgetter(1)))
        print('---')
        print(score_list)
        return max(score_list,key=itemgetter(1))
    
    
# Function to save a pickle file
def pickle_list(alist, name):
        with open(path + name + '.pkl', 'wb+') as file:
                pickle.dump(alist, file, pickle.HIGHEST_PROTOCOL)


# Function to pull pickle file
def unpickle_list(name):
    with open(path + name + '.pkl', 'rb') as file:
        return pickle.load(file)
    

# Function that takes an emotion dictionary and emotion word
#  then returns a dictionary with the associated emotion score
def get_score(dictionary, emotion_word):
    score_dict = dict()
    for d in dictionary:
        if d['word'] == emotion_word:
            score_dict['word'] = emotion_word
            score_dict['anger'] = d['anger']
            score_dict['anticipation'] = d['anticipation']
            score_dict['joy'] = d['joy']
            score_dict['trust'] = d['trust']
            score_dict['fear'] = d['fear']
            score_dict['surprise'] = d['surprise']
            score_dict['sadness'] = d['sadness']
            score_dict['disgust'] = d['disgust']
            return score_dict
    return score_dict


# Function that takes a list tuples strings (books/poems) and scores them
#  based on their emolex words
def emolex_score(booklist, dictlist):

    # List of book dictionaries  
    book_dict_list = []

    # Loop through all books in list
    #  use first element of book tuple
    for book in booklist:
        book_dict = {}
        book_dict['s'] = book[0]
        book_dict['id'] = book[1]
        # Create scoring class out of books
        scored_book = scored_text(book[0])
        print('Splitting Book #', book[1])
        # Splits entire book by words -- using a RegEx to take care of commas and apostrophes
        re_book = re.findall(r'\w+|\S+', scored_book)
        print('Book # ', book[1], ' split')
        # Look through entire book for emotion words
        for token in re_book:
            # Score potential emotion words
            #   add emotion scores to book score
            emotion_word_scores = get_score(dictlist, token)
            scored_book.add_score(emotion_word_scores)
        print('Book Score for Book # ', book[1])
        book_score = scored_book.return_max_score()
        print()
        book_dict['emotion'] = book_score
        book_dict_list.append(book_dict)
        
    return book_dict_list


def total_books(bookdictlist):
    
    # Initialize counters for each emotion
    #  count number of books in each type of emotion category
    joy = 0
    trust = 0
    anger = 0
    sadness = 0
    anticipation = 0
    disgust = 0
    fear = 0
    surprise = 0

    # Create a list for the scores
    score_list = []

    for book in bookdictlist:
        score_list.append(book['emotion'][0])
        if book['emotion'][0] == 'joy':
            joy += 1
        if book['emotion'][0] == 'trust':
            trust += 1
        if book['emotion'][0] == 'sadness':
            sadness += 1
        if book['emotion'][0] == 'anticipation':
            anticipation += 1
        if book['emotion'][0] == 'surprise':
            surprise += 1
        if book['emotion'][0] == 'fear':
            fear += 1
        if book['emotion'][0] == 'disgust':
            disgust += 1
        if book['emotion'][0] == 'anger':
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

    

# Main Function
if __name__ == '__main__':

    # Path for files
    path = 'pickles/'

    # Create list of books from booklist pickle
    book_list = unpickle_list('booklist')

    # Create emolex dictionary from pickle file
    dict_list = unpickle_list('dictlist')

    # Create list of books and their scores
    book_dict_list = emolex_score(book_list, dict_list)
    
    # Save the pickle!!!
    pickle_list(book_dict_list, 'bookdictlist')

    # Show book scores 
    total_books(book_dict_list)

    
