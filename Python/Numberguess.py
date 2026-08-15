secret_number = 7
guess = int(input("Guess the number: "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    guess = input("Try again: ")

print("Congratulations! You guessed the number.")
print("The secret number was", secret_num)
