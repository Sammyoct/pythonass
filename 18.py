'''A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.'''

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
