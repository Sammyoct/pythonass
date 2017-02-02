#!/usr/bin/python

def sum_(a):
    x = 0
    for char in a:
        x = x + char         
    return x

def multiply_(b):
    x = 1
    for char in b:
        x = x * char
    return x

def get_start():
    a = [1,2,3,4]
    #b = raw_input("Please enter list:")
    #print "You have entered list as of ",a    
    #a = [b]
    x = sum_(a)
    y = multiply_(a)
    print "Sum is ===> ", x
    print "Multiply  is ===> ", y
    

get_start()
