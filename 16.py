'''Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.'''
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
    ss = raw_input("Enter the number to findout list of words that logner:")
    # = range(1,15)
    m = []
    cnt = ss
    word = []
    for x in j:
        if len(x) > cnt:
            word.append(x)
    
    print("list of words :",word)

find_longest_word() 
