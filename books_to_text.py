#books_to_text.py
# Program that will take a list of book dictionaries
#  then write to seperate text files based on the emotions they
#  are categorized as.
#
#UCCS REU for Machine Learning in NLP 2019
#Brendan Bena - July 9th, 2019
import os
import json
import gzip
import pickle
import itertools

# Function that will create the necessary directory structure
def dir_constructor():
    
    if os.path.exists('pickles/') == False:
        os.mkdir('pickles/')

    if os.path.exists('guten_text/') == False:
        os.mkdir('guten_text/')


# Function to save a pickle file
def pickle_list(alist, name):
        with open(path + name + '.pkl', 'wb+') as file:
                pickle.dump(alist, file, pickle.HIGHEST_PROTOCOL)


# Function to pull pickle file
def unpickle_list(name):
    with open(path + name + '.pkl', 'rb') as file:
        return pickle.load(file)

def to_emotion_text(bookdictlist):

    # place the json lines in to a list of dictionary
    lines = []
    for line in gzip.open('gutenberg-poetry-v001.ndjson.gz'):
        lines.append(json.loads(line.strip()))
    
    print('dictionary created')

    # loop through each id and
    #  appened emotion to each dictionary based on their GID
    for book in bookdictlist:
        for dictionary in lines:
            if dictionary['gid'] == int(book['id']):
                dictionary.update(emotion = book['emotion'][0])

    print('dictionary appending done')

    pickle_list(lines, 'emotiondictlist')

    with open('guten_text/angergutentext.txt','w+') as anger:
        for dictionary in lines:
            if dictionary['emotion'] == 'anger':
                    anger.write(dictionary['s']+'\n')
    anger.close()
    print('Anger Poems written')

    with open('guten_text/trustgutentext.txt','w+') as trust:
        for dictionary in lines:
            if dictionary['emotion'] == 'trust':
                    trust.write(dictionary['s']+'\n')
    trust.close()
    print('Trust Poems written')

    with open('guten_text/anticipationgutentext.txt','w+') as anticipation:
        for dictionary in lines:
            if dictionary['emotion'] == 'anticipation':
                    anticipation.write(dictionary['s']+'\n')
    anticipation.close()
    print('Anticipation Poems written')

    with open('guten_text/disgustgutentext.txt','w+') as disgust:
        for dictionary in lines:
            if dictionary['emotion'] == 'disgust':
                    disgust.write(dictionary['s']+'\n')
    disgust.close()
    print('Disgust Poems written')

    with open('guten_text/sadnessgutentext.txt','w+') as sadness:
        for dictionary in lines:
            if dictionary['emotion'] == 'sadness':
                    sadness.write(dictionary['s']+'\n')
    sadness.close()
    print('Sadness Poems written')

    with open('guten_text/feargutentext.txt','w+') as fear:
        for dictionary in lines:
            if dictionary['emotion'] == 'fear':
                    fear.write(dictionary['s']+'\n')
    fear.close()
    print('Fear Poems written')

    with open('guten_text/surprisegutentext.txt','w+') as surprise:
        for dictionary in lines:
            if dictionary['emotion'] == 'surprise':
                    surprise.write(dictionary['s']+'\n')
    surprise.close()
    print('Surprise Poems written')

    with open('guten_text/joygutentext.txt','w+') as joy:
        for dictionary in lines:
            if dictionary['emotion'] == 'joy':
                    joy.write(dictionary['s']+'\n')
    joy.close()
    print('Joy Poems written')

if __name__ == '__main__':

    # Path for files
    path = 'pickles/'

    dir_constructor()

    # Grab book pickle
    book_dict_list = unpickle_list('bookdictlist')
    
    to_emotion_text(book_dict_list)
