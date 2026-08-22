a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print("Addition of the numbers: ", a + b)
print("Subtraction of the numbers: ", b-a)
print("Multiplication of the numbers: ", a * b)
if b>0:
  print("Division of the numbers: ", a / b)
  print("Integer division of the numbers: ", a // b)
  print("Remainder of the two numbers: ", a % b)
print(f"Exponentiation of the numbers: {a ** b}")
