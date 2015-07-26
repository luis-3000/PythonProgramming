""" This is a Pig Lating Translator
    It takes a word as a string, removes the first letter at
    the front, moves it to the back and apends 'ay' to the end."""
# Pig Latin
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:len(new_word)] + first + pyg
    print new_word
else:
    print 'empty'