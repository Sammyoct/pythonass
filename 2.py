#!/usr/bin/python

"""Define a function max_of_three() that takes three numbers as arguments and returns the largest of them."""


def max_val(a, b):
    """ Function to return if a is greater than b """
    if a < b:
        return True
    elif b < a:
        return False
    elif b == a:
        return "Equal"


def max_val_three(a, b, c):
    """ Function get value max out of three"""
    m = 0
    x = max_val(a, b)
    if x != "Equal":
        if x:
            m = b
        else:
            m = a
    else:
        m = a
    y = max_val(m, c)
    if x != "Equal":
        if y:
            m = c
        else:
            m = m
    else:
        m = m
    return m


def get_start():
    x = False
    var1 = raw_input("Please enter something var1: ")
    print "you entered", var1
    var2 = raw_input("Please enter something var2: ")
    print "you entered", var2
    var3 = raw_input("Please enter something var3: ")
    print "you entered", var3
    x = max_val_three(var1, var2, var3)
    print "max value ==> " + x

get_start()
