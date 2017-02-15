#!/usr/bin/python\
'''Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)'''
"""Get the lengtih of string manualy"""


def chk_len(a):
    """Function to find the length of the passed streing."""
    x = 0
    for c in a:
        x = x + 1

    return x


def get_start():
    x = 0
    var1 = raw_input("Please enter string: ")
    print ("you entered", var1)
    x = chk_len(var1)
    print ("Length ==> ", x)

get_start()
