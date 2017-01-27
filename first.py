#!/usr/bin/python
def max_val(a,b):
    if a < b:
        return True
    elif b < a:
        return False

def get_start():
    x = False 
    var1 = raw_input("Please enter something var1: ")
    print "you entered", var1
    var2 = raw_input("Please enter something var2: ")
    print "you entered", var2
    x = max_val(var1,var2)
    if x:
        print "max value ==> " + var2
    else :
        print "max value ==> " + var1


get_start()
