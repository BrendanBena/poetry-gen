# Creative Poetry Generation
Repo to host a creative poetry generation project implementation for the Summer 2019 UCCS REU in Machine Learning for Natural Language Processing.

## Collection dream data
To collect the dream data from _DreamBank.net_ that we used in our project run the .py files from the CL as follows:


  1. Extract dreams from the **DreamBank**
  ```
  python2 dream_extractor.py
  ```
  *Currently, this project requires using Python2 for the dream_extractor.py script*


  2. Convert json objects into a .txt file
  ```
  python3 dreamjson_to_text.py
  ```
These python scripts will create the directory structure necessary to scrape and create .txt files in the directory you are currently in.
