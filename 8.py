#!/usr/bin/python

def get_start():
    b = raw_input("Please entering the string:")
    print "you have entered string", b

    a = b

    s = list(a)
    j = []

    for x in reversed(s):
        j.append(x)

    n = "".join(str(x) for x in j)

    if n == a:
        print True
    else:
        print False

get_start()
