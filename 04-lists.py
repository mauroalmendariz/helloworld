print("We're making lists!")

# create the list
thisIsAList = []
secondList = ["first", "second", "third"]
# populate the list
thisIsAList.append(1)
thisIsAList.append(2)
thisIsAList.append(3)
# print the list
print(thisIsAList[0]) # prints 1
print(thisIsAList[1]) # prints 2
print(thisIsAList[2]) # prints 3
# print the list iteratively
for x in thisIsAList:
    print(x)
#add another element to list.
thisIsAList.append(4)
print(thisIsAList[3])
# print the second list
for x in secondList:
    print(x)