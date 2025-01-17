# modules.py
# import from the classes module
from _11classes import *

# Creating our first client in this file.
modulesClient = ClientIdentity()
modulesClient.ClientName = "ModulesClient"
modulesClient.PrintMessage()
print(modulesClient.ClientName)

# Create a number holder and then print out value.
modulesNumber = NumberHolder(23)
print(modulesNumber.returnNumber())