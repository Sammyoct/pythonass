#!/usr/bin/python

def is_member(a,b):
    for x in a:
        for y in b:
            if x == y:
                return True

    return False

def get_input():
    b = raw_input("Please enter element:")
    return b

def get_start():
    a = []
    b = []
    s = raw_input("Please enter n for end of list")
    while s != 'n':
        s = get_input()
        if s != 'n':
            a.append(s)

    for x in a:
        print(x)

    s1 = raw_input("Please enter n for end of list")
    while s1 != 'n':
        s1 = get_input()
        if s1 != 'n':
            b.append(s1)

    for x in b:
        print(x)

    if is_member(a,b):
        print "Yes member of list exists"
    else:
        print "No not member of list exists"

get_start()
