# l1 = [2, 77, 12, 3, 0, 112, 4, -987]
#
# l2 = [x * 2 if x < 5 else x - 2 for x in l1]
#
# print(l2)

# l1 = ['Valentin', 'Petro', 'Anna', 'Evgen', 'Kostyantin', 'Valeriya', 'Yuliya']
#
# l2 = [x for x in l1 if len(x) <= 5]
#
# print(l2)

import datetime
import re

l1 = ['Ottawa', 'Moscow', 'Beijing', 'Polotsk', 'Versailles', 'Delhi', 'Cairo']

# 1 ----- #

start1 = datetime.datetime.now()

for i in range(1000000):
    i += i

l2 = [re.sub("[AEIOUY]", "", x.upper()) for x in l1]

print("Time: ", (datetime.datetime.now() - start1).microseconds)
print(l2)

# 2 ----- #

start2 = datetime.datetime.now()

for i in range(1000000):
    i += i

l2 = [elem.upper() for x in l1 for elem in x if elem.upper() not in "AEIOUY"]
# l2 = [letter.upper() for word in l1 for letter in word if letter not in "AEIOUY"]

print("Time: ", (datetime.datetime.now() - start2).microseconds)
print(l2)

# 3 ----- #

start3 = datetime.datetime.now()

# print(start3)

for i in range(1000000):
    i += i

l2 = []

for x in l1:
    s = ""
    for elem in x:
        if elem.upper() not in "AEIOUY":
            s += elem.upper()
    l2.append(s)

# end = datetime.datetime.now() - start3
# print(end)

print("Time: ", (datetime.datetime.now() - start3).microseconds)
print(l2)
