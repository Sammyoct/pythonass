#!/usr/bin/python
"""The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one."""
def get_input():
    a = int(raw_input("Please enter the number to repeat character:"))
    print "you have enter numember:",a
    return a

def get_max_of_list():
    j = []
    s = int(raw_input("end of inputs with  1"))
    while s != 1:
        s = get_input()
        if s != 1:
            j.append(s)

    # = range(1,15)
    j.sort()
    print j  
    print j[len(j)-1]
    
     
get_max_of_list()
