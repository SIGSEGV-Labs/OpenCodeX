
#this program is used to generate a random password 

import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
         'q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','*','(',')','+']
print("Welcome to password generator!......")
n_letters=int(input("How many letters you want..."))
n_symbols=(input("How many symbols you want...")
n_numbers=int(input("How many numbers you want..."))
password_list=[]
for i in range(1,n_letters):
    char=random.choice(letters)
    password_list.append(char)

for i in range(1,n_symbols):
    char=random.choice(symbols)
    password_list.append()

for i in range(1,n_numbers):
    char=random.choice(numbers)
    password_list.append()

print(password_list)

random.shuffle(password_list)
print(password_list)
password=""
for i in password_list:
    print(password) 

