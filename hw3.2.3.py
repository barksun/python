# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

arg_1 = int(input("arg_1 = "))
arg_2 = int(input("arg_2 = "))
arg_3 = int(input("arg_3 = "))


def my_func(arg_first, arg_second, arg_third):
    list_arg = [arg_first, arg_second, arg_third]
    max_num1 = max(list_arg)
    list_arg.remove(max_num1)
    max_num2 = max(list_arg)
    return max_num1 + max_num2

print(my_func(arg_1, arg_2, arg_3))