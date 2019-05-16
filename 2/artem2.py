import random
from locale import str

x = random.randint(1, 10)
y = input("Загадайте число:")
print("Я загадал число " + str(x))
if x == int(y):
    print("Я угадал!!!!!!!!!!!!!!!!!!!!")
else:
    print("Я проиграл...")