# Creative Poetry Generation
Repo to host a creative poetry generation project implementation for the Summer 2019 UCCS REU in Machine Learning for Natural Language Processing.

This repo shows how to completely reproduce my UCCS REU in ML for NLP research project. The project involves taking a state of the art language model, OpenAI's GPT-2 (a Transformer Neural Network architecture), and finetuning the model on various sets of data, then using that model for text generation. We explore different forms of influencing natural language generation with things such as emotion-infused and dream text.

## Data Collection & Preparation
The following section outlines the necessary steps to complete the initial data collection and pre-processing of our project.

  #### Collection of dream data
  To collect the dream data from _DreamBank.net_ that we used in our project run the .py files from the CL as follows:
    
   ```
   python2 dream_extractor.py
   ```
   *Currently, this project requires using Python2 for the dream_extractor.py script*
   
   ```
   python3 dreamjson_to_text.py
   ```
   These python scripts will create the directory structure necessary to scrape and create .txt files in the directory you are    currently in.

  #### Creation of EmoLex Python dictionary
  
  Begin by downloading the "Non-Commercial Research Use" version of EmoLex from the lexicon home here:
  
  http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm 
  
  Next place the zipped EmoLex folder in the project directory.
  
  The following .py file will create an emo_lex directory, unzip the folder, and create the emolex dictionary. 
  
  Run it from the CL as follows:

   ```
   python3 emolex_to_dict.py
   ```
   A .pkl file is saved in the "/pickles" directory for later use
   
   #### Collection of GutenBerg Corpus
   The original version of this project makes use of the GutenTag tool to collect a corpus, but for quick and easy replication we recommended making use of Allison Parrish's gutenberg-poetry-corpus at https://github.com/aparrish/gutenberg-poetry-corpus.
   
   This corpus has been filtered based on some heuristics (see GitHub page) and contains (mostly) only-English text.
   
   Place the zipped json folder in the project directory after downloading from here:
   http://static.decontextualize.com/gutenberg-poetry-v001.ndjson.gz
   
   After downloading the data run the following .py file to create a .pkl list of the book's string and ID tuples:
   ```
   python3 gutentext_to_books.py
   ```
  
  #### Poem Emotion Scoring
  The following scripts contains a 'scored_text' class that ranks a text based on the number of EmoLex words found in it. 
  
  Run the following command to score a string and ID tuple list of books:
  ```
  python3 books_scorer.py
  ```
  This will create a book dictionary list .pkl in the form:
  
  \[{'s':'book_string', 'id': int, emotion:('emolex_emotion','numberofemotionwords')},...]
  
  The next command will use the book dictionary to write to seperate .txt files based on emotion categories:
  
  ```
  python3 books_to_text.py
  ```
  
  
  Thats it! You know should have all data necessary to rerun our experiment.

## Re-Training GPT-2
  This sections outlines how to finetune our preprocessed data using Google Colab and the gpt-2-simple Python package.
  
  Start by uploading your .txt files to the main directory of your Gooogle Drive. 
  
  Next make a copy of the Colab we make use of here: 
  https://colab.research.google.com/drive/1zaZOYw0a3uYx09J-GdtS-9TSC44_ONSv
  
  The Colab will give you directions to complete the experiments.
 
