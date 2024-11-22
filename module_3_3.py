def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(b=25)       # вызов работает, но PyCharm не нравится, что меняется тип переменной
print_params(c=[1,2,3])  # вызов работает, но PyCharm не нравится, что меняется тип переменной, к тому же список

values_list = [13, 'String', 5.3]
values_dict = {'a': 5, 'b': 'Словарь', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['World', 6.09]
print_params(*values_list_2, 42)