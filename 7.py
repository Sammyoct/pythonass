#!/usr/bin/python
'''Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".'''
def get_start():
    a = "I am testing"
    s = list(a)
    j = []

    for x in reversed(s):
        j.append(x)

    n = "".join(str(x) for x in j)

    print n

get_start()
