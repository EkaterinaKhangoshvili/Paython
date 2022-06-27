income = int(input("Укажите сумму вашей выручки - "))
expense = int(input("Укажите общую сумму расходов - "))
marg = (income - expense)/income*100
profit = income - expense
if income > expense:
    print("Отличный результат, получена прибыль ",profit)
    print("Рентабельность выручки составила ",marg,"процентов")
    people = int(input("Укажите численность сотрудников - "))
    print("Прибыль в рассчете на одного сотрудника составляет - ",profit / people)
    print("Конец программы")
else:
    print("Результат отрицательный, сумма убытков ",income - expense)
    print("Конец программы")

