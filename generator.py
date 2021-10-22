import sys
import random
import string


password = []
characters_left = -1


def update_characters_left(number_of_characters):
    global characters_left
    while True:
        if number_of_characters < 0 or number_of_characters > characters_left:
            print("The number of characters exceeds the number of free characters: ", characters_left)
            number_of_characters = int(input("Enter a valid value"))
        else:
            characters_left -= number_of_characters
            break


while True:
    password_length = int(input("How long the password should be: "))

    if password_length < 5:
        print("Password must be at least 5 characters long, please try again")
    else:
        characters_left = password_length
        break

print("Remaining characters: ", characters_left)

lowercase_letters = int(input("How many lowercase letters should the password have: "))
update_characters_left(lowercase_letters)
print("Remaining characters: ", characters_left)

uppercase_letters = int(input("How many uppercase letters should the password have: "))
update_characters_left(uppercase_letters)
print("Remaining characters: ", characters_left)

special_characters = int(input("How many special characters should the password have: "))
update_characters_left(special_characters)
print("Remaining characters: ", characters_left)

digits = int(input("How many digits should the password have: "))
update_characters_left(digits)
print("Remaining characters: ", characters_left)

if characters_left > 0:
    print("Not all characters have been used. The password will be completed with lowercase letters")
    lowercase_letters += characters_left

print()
print("Password length: ", password_length)
print("Lowercase letters: ", lowercase_letters)
print("Uppercase: ", uppercase_letters)
print("Special characters: ", special_characters)
print("Digits: ", digits)

for i in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice((string.ascii_uppercase)))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        password_length -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Password: ", "".join(password))


