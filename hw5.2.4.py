# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
my_f = open("text_4.txt", "r", encoding="utf-8")
content = my_f.read().split("\n")
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
for i in content:
    i = i.split(' ',1)
    new_file.append(rus[i[0]] + '  ' + i[1])
print(new_file)
my_f_2 = open('text_4_new.txt', 'w', encoding="utf-8")
my_f_2.writelines(new_file)