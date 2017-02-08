'''Write a function find_longest_word() that takes a list of words and returns the length of the longest one.'''
#!/usr/bin/python
def get_input():
    a = raw_input("Please enter word:")
    print "you have entered word:",a
    return a

def find_longest_word():
    j = []
    s = raw_input("end of inputs with  n")
    while s != 'n':
        s = get_input()
        if s != 'n':
            j.append(s)

    # = range(1,15)
    m = []
    cnt = 0
    for x in j:
        if len(x) > cnt:
            cnt = len(x)
            word = x
    
    print("Max word is :",word)

find_longest_word() 
