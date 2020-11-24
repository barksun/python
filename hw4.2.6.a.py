# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,

# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.

from itertools import count
for el in count(3):
    if el > 10:
        break
    else:
        print(el)