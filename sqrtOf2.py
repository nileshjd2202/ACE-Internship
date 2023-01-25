x = 8

if x<= 1:
    print(x)

low = 1
high = x//2

while(low<high):
    mid = ((low+high)//2 +1)
    div = x//mid
    if div == mid:
        print(mid)
    if div < mid:
        high = mid-1
    else:
        low = mid
print(low)