# Basic class for an identity manager.
class ClientIdentity:
    ClientName = "blah"

    def PrintMessage(self):
        print("This is a message from a class function.")

# Basic class for holding a number.
class NumberHolder:
    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number

# Create our first client.
firstClient = ClientIdentity()

# Use our function from inside the class.
firstClient.PrintMessage()

# Print the client's name using the simple print function.
print(firstClient.ClientName)

# Create our second client, assign unique name, use print function
# and print the unique name.
secondClient = ClientIdentity()
secondClient.ClientName = "Mauro"
secondClient.PrintMessage()
print(secondClient.ClientName)

firstNumber = NumberHolder(8)
print(firstNumber.returnNumber())