#!/usr/bin/python
'''Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.'''


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


def get_input():
    b = int(raw_input("Please enter list:"))
    print "You have entered list as of ", b
    return b


def get_start():
    a = []

    s = raw_input("End of list press n")
    while s != 'n':
        g = get_input()
        a.append(g)

    for j in a:
        print(j)

    x = sum_(a)
    y = multiply_(a)
    print "Sum is ===> ", x
    print "Multiply  is ===> ", y


get_start()
