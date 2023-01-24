d = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_d)

from operator import itemgetter
 
list = [{"name": "Nandini", "age": 20},
        {"name": "Manjeet", "age": 20},
        {"name": "Nikhil", "age": 19}]
 
# using sorted and itemgetter to print list sorted by age
print(sorted(list, key=itemgetter('age')))