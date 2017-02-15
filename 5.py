#!/usr/bin/python
"""Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")should return the string "tothohisos isos fofunon"."""


def get_input():
    b = raw_input("Please enter string to convert into robbers language:")
    return b


def get_start():
    s = get_input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = list(s)

    j = []
    for x in s:
        if x != " ":
            if x not in vowels:
                j.append(x)
                j.append("o")
                j.append(x)
            else:
                j.append(x)

    j = "".join(str(x) for x in j)
    print j


get_start()
