#!/usr/bin/python


def get_input():
    a = raw_input("Please enter the number to repeat character:")
    print "you have enter numember:",a
    return a

def get_list_lengths_in_list():
    j = []
    s = raw_input("end of inputs with  n")
    while s != 'n':
        s = get_input()
        if s != 'n':
            j.append(s)

    # = range(1,15)
    m = []
    for x in j:
        m.append(len(x))
    
    print j
    print m 
    
get_list_lengths_in_list()    
