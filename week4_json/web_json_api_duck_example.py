'''
This program queries datamuse for words associated with a given word.
The associated words are given a score.
'''

import requests
import json

# example url to query datamuse web json api
example_url = "https://api.datamuse.com/words?ml=duck"

# variables to query alphavantage
word = 'duck'
key_word = "word"
key_score = "score"
search_word = "mallard"

#generate url
#url = 'https://api.datamuse.com/words?ml=' + word
#print(url)

# requests stock data from data muse
#request = requests.get(url)
# print(request.text) # print to double check data from web json api is good
#dct_full = json.loads(request.text)




#####################################################################
# programming activity
# What is the score of the associated word: mallard
# Steps: 
# 1. load json into a dictionary
# 2. search for word "mallard"
# 3. print associated score value for mallard

# answer below, try yourself before looking


# Get duckling
# Looping through a list of dictionaries - for loop with if statement to find duckling
for dictionary in data



























#for dct_small in dct_full:
#     # print(dct_small) # print all values to verify data is good
#     if dct_small[key_word] == search_word:
#         print("word: ", dct_small[key_word])
#         print("value: ", dct_small[key_score])
#        



























"""
This program queries Datamuse for words associated with a given word.
The associated words are given a score.
"""

import requests
import json

# Base word you want related terms for
word = 'duck'

# Ask user for the search word (replace with "duckling" if you want to hardcode it)
search_word = input("duckling").strip().lower()

# Keys used in the Datamuse JSON response
key_word = "word"
key_score = "score"

# Generate URL
url = f'https://api.datamuse.com/words?ml={word}'
print(f"Querying: {url}")

# Request data from Datamuse
request = requests.get(url)
dct_full = json.loads(request.text)

# Search for the user-provided word
found = False
for dct_small in dct_full:
    if dct_small[key_word].lower() == search_word:
        print(f"word: {dct_small[key_word]}")
        print(f"score: {dct_small[key_score]}")
        found = True
        break

if not found:
    print(f"'{search_word}' not found in Datamuse results for '{word}'.")
