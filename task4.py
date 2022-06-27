num_1 = int(input("Введите число - "))
a = 0

while (num_1):
    if (num_1 % 10 > a):
        a = num_1 % 10
    num_1 //= 10

print("Наибольшая цифра в числе", a)
print("Конец программы")