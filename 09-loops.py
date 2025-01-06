#for loops
numbers = [2, 3, 4, 5]
for number in numbers:
    print(number)

#while loops
count = 0
while count < 5:
    print(count)
    count += 1

#while loop printing 1-5 and then "break" out
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

#for loop that skips even numbers and only print odds. 
count = 0
for x in range(10):
    # Check if x is even.
    if x % 2 == 0:
        continue
    print(x)

# Else in a for loop.
count = 0
for x in range(5):
    # Check if x is odd.
    if x % 2 == 0:
        print(x)
    else:
        print("This is supposed to be an odd number.")