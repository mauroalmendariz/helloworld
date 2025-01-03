#This prints out "Hello, John!"
name = "Mauro Almendariz"
print("Hello, %s!" % name) #This is how to print a string, but with the option to place specific text at a place.

#Using a tuple - %s %d (arg1, arg2)
#This prints out "Mauro Almendariz is 35 years old."
age = 35
print("%s is %d years old." % (name, age))

#The %s operator will string format other non-string variables.
myList = [1, 2, 3]
print("A list: %s" % myList)

#Printing a bunch of numbers.
print("The %d-%d Dallas Cowboys are playing the %d-%d Washington Commanders in Week 17 to close the season." % (7, 9, 11, 5))
#Printing the Cowboys win percentage.
cowboysWinPercentage = 7.0 / 9.0
print("Cowboys Win %%: %.2f" % cowboysWinPercentage)
