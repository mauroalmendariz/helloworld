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

### Using the Functions ###
helloWorld()
helloWorldTwo("Hello World!")
numberOne = 4
numberTwo = 3
print(sumOfArguments(numberOne, numberTwo))

