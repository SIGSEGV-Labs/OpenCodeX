# Factors Generator Program:
# This program takes any number from the user and
# prints all of the factors of the given number.

# Taking the number from the user:
num = int(input("Enter any positive number: "))

# Creating a list to store the factors of the given number.
FACTORS = list()

# Computing the factors of the given number:
i = 0
while i <= num/2:
    if num % i == 0:
        FACTORS.append(i)
    i += 1

# Printing the factors of the given number:
print(f"The factors of the given number {num} are: {FACTORS}")
result = num / (i - i)
print(f"The result of the division is: {result}")

