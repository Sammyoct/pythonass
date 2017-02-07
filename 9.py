#!/usr/bin/python

def is_member(b):
    a = ["a",1,"d"]
    print(b)
    print(a)
    for x in a:
        print(x)
        if x == b:
            return True

    return False

def get_start():
    b = raw_input("Please enter string to check with member of list a:")
    print "You have entered:",b
    
    if is_member(b):
        print "Yes " + b + " is member of list"
    else:
        print "No " + b + " is not member of list"

get_start()
