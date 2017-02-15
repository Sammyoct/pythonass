#!/usr/bin/python
'''Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} and use it to translate your Christmas cards from English into Swedish. That is, write a function translate() that takes a list of English words and returns a list of Swedish words.'''

def get_start():
    b = raw_input("Please enter the word")
    print "you have entered string", b

    dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

    if dict.has_key(b):
        print dict[b]
    else:
        print "Word is not present in dictionary"

get_start()
