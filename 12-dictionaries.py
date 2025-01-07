# Create dictionary, add values, and print.
phonebook = {}
phonebook["John"] = 123456789
phonebook["Jack"] = 213457689
phonebook["Jill"] = 312754698
print(phonebook)

# Create another dictionary in a different way. Same results.
phonebookTwo = {
    "Earl" : 213457689,
    "Eric" : 312754698,
    "Evan" : 123456789
}
print(phonebookTwo)

# Dictionary iteration.
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Deleting an entry.
del phonebookTwo["Evan"]
# Print to confirm.
print(phonebookTwo)
# Delete with .pop.
phonebookTwo.pop("Earl")
print(phonebookTwo)