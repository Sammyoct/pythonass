#!/usr/bin/python

def get_start():
    a = "I am testing"
    s = list(a)
    j = []

    for x in reversed(s):
        j.append(x)

    n = "".join(str(x) for x in j)

    print n

get_start()
