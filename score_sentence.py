#score_sentence.py
# Program to take a sentence string and
#  and score said sentence using values from
#  the compiled NRC EmoLex dictionary
#
#UCCS REU for Machine Learning in NLP 2019
#Brendan Bena - June 20th, 2019

import pickle
import inspect
from operator import itemgetter

# Path for generated pickle files
path = 'pickles/'

# Function to pull dictionary file from pickle file
def unpickle_list(name):
    with open(path + name + '.pkl', 'rb') as file:
        return pickle.load(file)

# Pull EmoLex dictionary from pickle file 
emolex_dict = unpickle_list('dictlist')

# Class to hold a score emotion sentence
class scored_sentence(str):
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


# Function that takes a dictionary and emotion word
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
