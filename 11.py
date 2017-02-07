#!/usr/bin/python

def generate_n_chars(a,b):
    j = []
    for x in list(range(int(a))):
        j.append(b) 

    j = "".join(str(x) for x in j)
    print j

def get_input():
    a = raw_input("Please enter the number to repeat character:")
    print "you have enter numember:",a
    b = raw_input("Please enter the character:")
    print "you have enter numember:",b

    generate_n_chars(a,b)

get_input()
