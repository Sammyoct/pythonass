#!/usr/bin/python
'''Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")should return the string "tothohisos isos fofunon".'''
class RobbersLanguage():

    def __init__(self):
        self.string = raw_input ("Enter the string: ")

    def convert(self):
        vowels = ['a','e','i','o','u']
        s = list(self.string)

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
        return j



x = RobbersLanguage()
print (x.convert())
