n = 3

pre1,pre2 = 1,1

for i in range(2,n+1):
    curr  = pre1 + pre2
    pre2 = pre1
    pre1 = curr

print(pre1)