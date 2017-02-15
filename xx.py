#!/usr/bin/python
p = filter(lambda x: x % 2, range(1, 100000))
s = []
for num in p:
    if all(num%i !=0 for i in range(3,num)):
        s.append(num)
print s
