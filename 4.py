#!/usr/bin/python

def chk_vowel(a):
    vowel = ['a','e','i','o','u']
    for char in vowel:
         if char in a:
             return True 
             
    return False

def get_start():
    x = False
    a = raw_input("Please enter only one character:")

    while len(a) != 1:
        a = raw_input("Please enter only one character:")
        print "You have entered", a

    x = chk_vowel(a)
    print x
    

get_start()
