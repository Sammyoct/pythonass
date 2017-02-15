'''A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.'''

import string

def is_pangram(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in phrase:
            return False

    return True

def get_start():
    b = raw_input("Please enter the string:")
    print "you have entered string", b

    index = 0

    a = []
    for char in b:
        if char not in string.punctuation and char not in string.whitespace:
            
            a.append(char)

    a = "".join(str(x) for x in a)

    a = a.lower()

    s = list(a)


    if is_pangram(s):
        print("Yes given string is pangram")
    else:
        print("No given string is not pangram")

get_start()
