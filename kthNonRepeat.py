# K’th Non-repeating Character in Python using List Comprehension and OrderedDict

from collections import OrderedDict

stng = 'aceerpsolution'
dict1 = OrderedDict.fromkeys(stng,0)

for ch in stng:
    dict1[ch] += 1

nonrepeatDict = [key for key,value in dict1.items() if value==1]

if len(nonrepeatDict)<3:
    print("Less than k non-repeating characters")
else:
    print(nonrepeatDict[3-1])
