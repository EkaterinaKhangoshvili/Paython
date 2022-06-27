one_day = int(input("Введите результат спортсмена в первый день - "))
finish = int(input("Введите желаемый результат - "))
day = 1
while one_day <= finish:
    print(day,"-й день:",one_day)
    one_day = one_day + (0.1 * one_day)
    day = day + 1

print("на",day,"день спортсмен достиг результата — не менее",finish,"км.")



