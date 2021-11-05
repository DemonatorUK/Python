mass = []
temp = 0
for i in range(1, 1001, 2):
    if (sum(map(int, str(i ** 3))) % 7) == 0:
        temp = temp + i ** 3
        mass.append(i ** 3)
print("Сумма всех чисел:", temp)
temp = 0
for i in mass:
    if (sum(map(int, str(i + 17))) % 7) == 0:
        temp = temp + i
print("Новая сумма всех чисел:", temp)


