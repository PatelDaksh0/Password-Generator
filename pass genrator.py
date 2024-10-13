import random

print('Welcome to Password Generator')
chars = 'abcdefghijklmnopqrstuvwxyz0987654321!@#$%^&*().,'
number = int(input('Amount of passwords to generate:\n'))
length = int(input('Input your password length:\n'))

print('\nHere are your passwords:')

for _ in range(number):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    print(password)
