#intro
x = 2
print(x == 2) #true
print(x == 3) #false
print(x < 3) #true

#and or
myName = "mauro"
myAge = 35
if myName == "mauro" and myAge == 35:
    print("This dude is mauro and he's also 35 years old.")

if myName == "mauro" or myName == "miguel":
    print("This gentleman's name is either mauro or miguel.")

# check if the string is in a list
lastName = "almendariz"
if lastName in ["almendariz", "glover"]:
    print("Your last name is either almendariz or glover")

# if statements
statement = False
otherStatement = True

if statement is True:
    print("You are pregnant!")
elif otherStatement is True:
    print("You are having twins!!")
else:
    print("You are not pregnant...")

# the is operator evaluates the instance, not the value
x = [1,2,3]
y = [1,2,3]
# this prints true because it's testing the values
print(x == y)
# this prints out false because they are two different things in memory
print(x is y)

# the not operator inverts the test
print(not False) #prints true
print((not False) == (False)) #print false