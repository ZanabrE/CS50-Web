# This line of code will give you an error 
# because the input function takes user input 
# as string.
# n = input("Number: ")

# Adding the int (integer) infront of the input
# ensures that the value entered is treated as a 
# number.

n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")
