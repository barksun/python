# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int (input("Введите значение выручки = "))
cost = int (input("Введите значение издержек = "))
# c - прибыль
profit = revenue - cost
# d - рентабельность
profitability = profit / revenue
# y - прибыль на одного сотрудника
if profit > 0:
    print ("Фирма приносит прибыль")
    print ("Рентабельность =",profitability)
    size = int (input("Введите численность сотрудников = "))
    profitbyemployee = profit / size
    print("Прибыль на одного сотрудника =",profitbyemployee)
else:
    print ("Фирма приносит убыток")
