#!/usr/bin/env python3

from collections import defaultdict
import json
import re

LETTER_STRENGTHS = {
    'E': 11.1607,
    'A': 8.4966,
    'R': 7.5809,
    'I': 7.5448,
    'O': 7.1635,
    'T': 6.9509,
    'N': 6.6544,
    'S': 5.7351,
    'L': 5.4893,
    'C': 4.5388,
    'U': 3.6308,
    'D': 3.3844,
    'P': 3.1671,
    'M': 3.0129,
    'H': 3.0034,
    'G': 2.4705,
    'B': 2.0720,
    'F': 1.8121,
    'Y': 1.7779,
    'W': 1.2899,
    'K': 1.1016,
    'V': 1.0074,
    'X': 0.2902,
    'Z': 0.2722,
    'J': 0.1965,
    'Q': 0.1962,
}

RE_ONLY_LETTERS = re.compile(r'^[A-Z]+$', re.IGNORECASE)

# Read /usr/share/dict/words into list
with open('/usr/share/dict/words', 'r') as f:
    words = f.read().splitlines()

# Create a dictionary of words with their lengths as keys
words_by_length = defaultdict(list)

# Populate the dictionary with words grouped by length
for word in words:
    if RE_ONLY_LETTERS.match(word):
        words_by_length[len(word)].append(word.upper())

# Sort each list of words by the strength of their letters
for length, word_list in words_by_length.items():
    words_by_length[length] = sorted(word_list, key=lambda word: sum(LETTER_STRENGTHS[letter] for letter in set(word)), reverse=True)

# Delete words with only one letter
del words_by_length[1]

# Convert the dictionary to a JSON string
json_data = json.dumps(words_by_length)

# Write the JSON string to a file
with open('word-list.json', 'w') as f:
    f.write(json_data)
