### Defining Functions ###

#function that prints "Hello World!"
def helloWorld():
    print("Hello World!")

# Function that prints argument.
def helloWorldTwo(stringOne):
    print(stringOne)

# Function that returns a sum.
def sumOfArguments(numberOne, numberTwo):
    return numberOne + numberTwo

# One function to call them all!
def callThemAll(stringOne, numberOne, numberTwo):
    helloWorld()
    helloWorldTwo(stringOne)
    sumOfArguments(3, 7)

### Using the Functions ###
callThemAll("Hello World!", 3, 7)

