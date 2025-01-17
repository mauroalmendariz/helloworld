# modules.py
# import from the classes module
import _11classes

# Creating our first client in this file.
modulesClient = _11classes.ClientIdentity()
modulesClient.ClientName = "ModulesClient"
modulesClient.PrintMessage()
print(modulesClient.ClientName)