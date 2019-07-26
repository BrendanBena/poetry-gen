#dreamjson_to_dict.py
# Program that will take json files of dreams and convert them to text files suited for training data
#
#UCCS REU for Machine Learning in NLP 2019
#Brendan Bena - July 22nd, 2019

import json
import os

# Paths for opening dream file directory and write file path
openpath='dream_text/'
writepath='dreams/'

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
