# input 
s = "LVIII" # answer = 58
dict1 = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

ans = 0
for i in range(0,len(s)-1):
    if dict1[s[i]] < dict1[s[i+1]]:
        ans -= dict1[s[i]]
    else:
        ans += dict1[s[i]]

ans += dict1[s[len(s)-1]]
print(ans)