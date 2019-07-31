#emolex_to_dict.py
# Program to convert the NRC Emotion Lexicon (EmoLex)
#  into a list of dictionaries.
#  dictionaries include the word and each emotion 
#  + there associated scores
#
#UCCS REU for Machine Learning in NLP 2019
#Brendan Bena - June 19th, 2019

import pandas as pd
import os
import pickle

# Function that will create the necessary directory structure
def dir_constructor():
    
    if os.path.exists('pickles/') == False:
        os.mkdir('pickles/')


# Function to save a pickle file
def pickle_list(alist, name):
        with open(path + name + '.pkl', 'wb+') as file:
                pickle.dump(alist, file, pickle.HIGHEST_PROTOCOL)


# Function to create a dictionary out of the emolex file
def emolex_to_dict():

    # Path for files
    path = 'pickles/'

    # Initialize dictionary list
    dictlist = []
                    
    # Read tsv file into Pandas dataframe object
    data = pd.read_csv("emo_lex/emolex.txt", sep='\t', names=['word', 'emotion', 'score'], header=None)

    # Loop through every 10th line and gather all necessary emotion words
    #  create dictionaries out of all words in emolex
    #   then append the dictionary to our list of dicts
    for i in range(0,len(data),10):	
        my_dict = { 'word' : data.loc[i,'word']}
        dictlist.append(my_dict)


    # Loop through every row in the dictionary
    #  look through every dictionary
    #   if word in row exists in the dictionary
    #    create dictionary out of the row for each emotion
    #
    # Those previous lines were probably confusing
    for i in data.index:
        print(i)
        for d in dictlist:
            if d['word'] == data.iloc[i,0]:
                temp_dict = { data.iloc[i,1] : data.iloc[i,2] }
                d.update(temp_dict)
    return dictlist


# Main Function
if __name__ == '__main__':

    dir_constructor()
    print('Create EmoLex dictionary')
    emolex_dict = emolex_to_dict()
    # Save the pickle!
    picklelist(emolex_dict, 'dictlist')
