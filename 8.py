#!/usr/bin/python
'''Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.'''
def get_start():
    b = raw_input("Please entering the string:")
    print "you have entered string", b

    a = b

    s = list(a)
    j = []

    for x in reversed(s):
        j.append(x)

    n = "".join(str(x) for x in j)

    if n == a:
        print True
    else:
        print False

get_start()
