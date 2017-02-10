#!/usr/bin/python
'''Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog:.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.'''

import string

def get_start():
    b = raw_input("Please entering the string:")
    print "you have entered string", b

    index = 0

    a = []
    for char in b:
        if char not in string.punctuation and char not in string.whitespace:
            a.append(char)

    a = "".join(str(x) for x in a)

    a = a.lower()

    s = list(a)
    j = []

    for x in reversed(s):
        j.append(x)

    n = "".join(str(x) for x in j)

    if n == a:
        print("Yes given string is palindrome")
    else:
        print("No given string is not palindrome")

get_start()
