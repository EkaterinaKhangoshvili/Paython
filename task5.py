income = int(input("Укажите сумму вашей выручки - "))
expense = int(input("Укажите общую сумму расходов - "))
if income > expense:
    print("Отличный результат, получена прибыль ",income - expense)
else:
    print("Результат отрицательный, сумма убытков ",income - expense)

print("Конец программы")
