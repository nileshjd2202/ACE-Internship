# input
nums = [2,7,11,15]
target = 9

dict1 = {}
        
for i, v in enumerate(nums):
    k = target-v
    if k in dict1:
        print([dict1[k],i])
    dict1[v] = i