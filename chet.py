list = list(map(int, input("Введите числа: ").split()))
n = 0
for a in list:
    if a % 2 == 0:
        n += 1
print("Количество четных чисел: ", n)
