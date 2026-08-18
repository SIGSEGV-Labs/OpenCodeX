# Prime Number Series Generator:
# This program generates Prime Number Series upto a given number.

# Taking the range from the user:
Nrange = int(input("Enter upto which number you want prime numbers: "))

i = 2
print(f"The Prime Numbers upto {Nrange} are: ", end = '')
while i <= Nrange:
    j = 2
    flag = 0

    while j <=i/2:
        if i % j == 0:
            flag = 1
            break
        j += 1

    if flag == 0:
        print(f"{i}", end = ' ')
    else:
        pass
    i += 1

print("\n")

