# Basic class for an identity manager.
class ClientIdentity:
    ClientName = "blah"

    def PrintMessage(self):
        print("This is a message from a class function.")

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