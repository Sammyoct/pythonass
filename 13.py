#!/usr/bin/python


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
