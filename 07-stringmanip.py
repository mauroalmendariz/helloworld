myString = "Ya Heard!"
#print the index where r first appears
print(myString.index("r"))
#print the total length
print(len(myString))
#print the number of a's in the string.
print(myString.count("a"))
#print from a specific starting point to a specific end point.
print(myString[4:7])

#print from the beginning the to the end.
print(myString[:])
#print to the fourth number.
print(myString[:4])

#print in reverse.
print(myString[::-1])

#toupper and tolower from C++ yay
print(myString.upper())
print(myString.lower())

#check if the string begins with "Ya". prints true
print(myString.startswith("Ya"))

#check if the string ends with "What". prints false
print(myString.endswith("What"))
