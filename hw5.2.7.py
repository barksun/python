#Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджеры контекста.
import json

zad7_list = []
my_dict_zad7 = {}
average_profit = {}
total_zad7 = 0

with open('text_7.txt', 'r', encoding='utf-8') as zadanie7:
    nums7 = zadanie7.read().splitlines()

for i in range(len(nums7)):
    a = nums7[i].split()
    my_dict_zad7[a[0]] = int(a[2]) - int(a[3])
    if (int(a[2]) - int(a[3])) > 0:
        total_zad7 += (int(a[2]) - int(a[3]))
average_profit['average_profit'] = total_zad7 / len(nums7)

zad7_list = [my_dict_zad7,average_profit]

with open('zadanie7.json', 'w') as zadanie7:
    zadanie7.write(json.dumps(zad7_list))