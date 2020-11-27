# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
my_f = open('test.txt', 'r')
content = my_f.read().split()
lines = 0
words = 0
letters = 0
for line in content:
    lines += 1
    letters += len(line)
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)
my_f.close()

