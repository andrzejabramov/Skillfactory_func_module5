import random


symbols_for_password = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def create_password_generator(n, symbols):
    def create_pass():
        password = ''
        for el in range(n):
            ind = random.randint(0, len(symbols) - 1)
            password = password + symbols[ind]
        return password
    return create_pass



password_generator = create_password_generator(10, symbols_for_password)
print(password_generator())
print(password_generator())