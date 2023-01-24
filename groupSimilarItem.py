# Python – Group Similar items to Dictionary Values List

# There are two methods: 1-> Using defaultdict() + loop , 2-> Using dictionary comprehension + Counter()

from collections import Counter

lst = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]

res = {key : [key] * val for key,val in Counter(lst).items()}

print(res)