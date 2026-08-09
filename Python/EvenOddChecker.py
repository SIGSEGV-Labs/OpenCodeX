# EvenNOdd Identifier
# This program checks whether the given number is even or odd.

# Taking the number input from the user:
x = input("Enter any number: ")

# Checking edge case:
if not x.lstrip("-").isdigit():
    print("Invalid Input!!")
    exit()

x = int(x)

# Validating whether the given number is even or odd:
if x % 2 == 0:
    print(f"{x} is an Even Number.")
else:
    print(f"{x} is an Odd Number.")
