# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

f_name = input("Имя: ")
s_name = input("Фамилия: ")


def my_f (first_name, second_name, year, city, email, phone):
    print (f"{first_name} {second_name} {year} {city} {email} {phone}")

my_f (first_name=f_name, city='Moscow', email='a@mail.ru', phone=495, second_name=s_name, year=1923)
