# There are two methods 1-> using loop, 2-> Using sorted() + lambda() + set() + values() + len()

test_dict = {"Gfg" : [5, 7, 5, 4, 5],
            "is" : [6, 7, 4, 3, 3], 
            "Best" : [9, 9, 6, 5, 5]}

max_key = sorted(test_dict, key = lambda ele: len(set(test_dict[ele])), reverse = True)[0]

print(max_key)