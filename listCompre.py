start = int(input("Enter starting index: "))

ending = int(input("Enter ending index: "))

list1 = [i for i in range(start,ending+1)]

dict1 = {x: x**2 for x in list1}

alreadyNum = set()
k = 0
while(k<3):
    user_input = int(input("Enter number to get square: "))
    val = dict1.get(user_input)
    if val:
        if user_input in alreadyNum:
            print("Already entered this number")
            k += 1
        else:
            print("Your output: " + str(dict1[user_input]))
        alreadyNum.add(user_input)
              
    elif k<3:
        k +=1 
        print("error: Number not in range")

print("Limit Over.")