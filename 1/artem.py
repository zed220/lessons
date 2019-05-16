def main():
    print("Привет, мир!!!!!!!!")
    print("Считаем сумму.")
    x = input("Введите первое число:")
    y = input("Введите второе число:")
    sum = artem3(int(x), int(y))
    print("Сумма равна " + str(sum))
    pass

def artem3(x, y):
    sum = int(x) + int(y)
    return sum

if __name__ == '__main__':
    main()