#!/usr/bin/python
""" Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example,histogram([4, 9, 7]) should print the following:
****
*********
*******"""

def generate_x_of_chars(a):
    j = []
    for x in list(range(int(a))):
        j.append("*") 

    j = "".join(str(x) for x in j)
    print j 

def get_input():
    a = raw_input("Please enter the number to repeat character:")
    print "you have enter numember:",a
    return a

def get_start():
    j = []
    s = raw_input("end of inputs with 'n'")
    while s != 'n':
        s = get_input()
        if s != 'n':
            j.append(s)

    for x in j:
        generate_x_of_chars(x)

get_start()
