#dreamjson_to_dict.py
# Program that will take json files of dreams and convert them to text files suited for training data
#
#UCCS REU for Machine Learning in NLP 2019
#Brendan Bena - July 22nd, 2019

import json
import os

# Function that will create the necessary directory structure
def dir_constructor():
    
    if os.path.exists('dream_text/') == False:
        os.mkdir('dream_text/')
        
# Function that gathers json dream objects
#  then writes them to a text file for use
def dream_to_text():
    
    # Paths for opening dream file directory and write file path
    openpath='dreams/'
    writepath='dream_text/'

    # Create file to write to
    dreamfile = open(writepath+"dreamtext.txt","w+")

    # Loop through all file in the directory
    for filename in os.listdir(openpath):
        # Create file out of directory filename and load JSON into a python dictionary
        myfile = open(openpath+filename, 'r')
        jsonobj = json.load(myfile)
        dictlist = jsonobj['dreams']
        # Loop through all the dictionary objects and pull the 'content' portion
        for dictobj in dictlist:
            # Write to text file
            dreamfile.write(dictobj['content'])
            dreamfile.write('/n')

    # Close the file
    dreamfile.close()

    print('Dreams Written')
    

# Main Function
if __name__ == '__main__':

    dir_constructor()
    print('Writing Dreams...')
    dream_to_text()
