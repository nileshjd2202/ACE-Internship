# Python – Find all duplicate characters in string using dictionary

from collections import Counter

stng = 'aceerpsolutions'

dict1 = Counter(stng)

for key,val in dict1.items():
    if(val>1):
        print(key, end=" ")

