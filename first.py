#!/usr/bin/python
'''Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)'''

def max_val(a, b):
    '''function returns the True/False/Equal value '''
    if a < b:
        return True
    elif b < a:
        return False
    elif b == a:
        return "equal"

def get_start():
    ''' x default value set as False '''
    x = False 

    '''get first variable'''
    var1 = raw_input("Please enter something var1: ")
    print "you entered", var1
    '''get second variable'''
    var2 = raw_input("Please enter something var2: ")
    print "you entered", var2
    x = max_val(var1, var2)
    if x != "equal":
        if x:
            print "max value ==> " + var2
        else:
            print "max value ==> " + var1
    else:
        print "values are equal"

get_start()
