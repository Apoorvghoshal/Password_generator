import random

print("*****************************************This is a Password Generator****************************************")
choice = input("Do you want passwords? (1 for Yes, 0 for No): ")
choice = int(choice)

while choice > 0:
    length = input("Enter the length of the password: ")
    length = int(length)
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ(),.@$!0123456789'
    print("Choose any of the following passwords:")

    for _ in range(8):
        password = ''
        for _ in range(length):
            password += random.choice(chars)
        print(password)

    choice = input("Do you want more passwords? (1 for Yes, 0 for No): ")
    choice = int(choice)
print("****************************************************Thank You************************************************")