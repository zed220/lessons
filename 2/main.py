import random

x = random.randint(1, 6)
y = input("Загадай число от 1 до 6:")
print("Моё число: " + str(x))
if int(x) == int(y):
    print("Я угадал!")
else:
    print("Я не угадал...")