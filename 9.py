#!/usr/bin/python
'''Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns Trueif x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)'''
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
