# Creative Poetry Generation
Repo to host a creative poetry generation project implementation for the Summer 2019 UCCS REU in Machine Learning for Natural Language Processing.

## Data Preparation
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
  To create a python version of the EmoLex dictionary file run the .py file from the CL as follows:

   ```
   python3 emolex_to_dict.py
   ```
   
   #### Collection of GutenBerg Corpus
   The original version of this project makes use of the GutenTag tool to collect a corpus, but for quick and easy replication we recommended making use of Allison Parrish's gutenberg-poetry-corpus at https://github.com/aparrish/gutenberg-poetry-corpus.
   
   This corpus has been filtered based on some heuristics (see GitHub page) and contains (mostly) only-English text.
   
   Download the Corpus here:
   http://static.decontextualize.com/gutenberg-poetry-v001.ndjson.gz
