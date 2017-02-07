#!/usr/bin/python
"""Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)"""

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
