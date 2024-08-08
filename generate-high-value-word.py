#!/usr/bin/env python3

import json
import re

RE_NOT_ALPHA = re.compile(r'[^A-Z]')

# Load the word list
with open('word-list.json') as f:
    word_list = json.load(f)

while True:
    # Input a word where some of the letters are unknown
    word_pattern = input('Enter the word pattern (use space for unknown letters): ').upper()

    word_length = str(len(word_pattern))
    print(f'Your word has {word_length} letters.')

    # Input letters that are definitely not in the word
    bad_letters = input('Enter the letters known to be absent from the word (or leave blank): ').upper()
    bad_letters = f"[^${RE_NOT_ALPHA.sub('', bad_letters)}]"

    # Input letters to give higher value
    required_letters = input('Enter the letters that should be present in the word (or leave blank): ').upper()
    required_letters = RE_NOT_ALPHA.sub('', required_letters)

    # Create a regex pattern using the word pattern where every unknown letter in the pattern is not bad_letters
    regex_pattern = re.compile('^' + ''.join(f'(?=.*{letter})' for letter in required_letters)
                               + ''.join(bad_letters if RE_NOT_ALPHA.match(letter) else letter for letter in word_pattern)
                               + '$')

    # Filter the word list based on the regex pattern and good letters
    filtered_words = (word for word in word_list[word_length] if regex_pattern.match(word))

    # Print the suggested words
    print(f"Suggested words: {', '.join(word for word, _ in zip(filtered_words, range(15)))}")
    print('\n')
