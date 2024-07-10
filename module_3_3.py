def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [54.32, False, 'Строка']
values_dict = {'a': True, 'b': 52, 'c': 'Писятдва'}
values_list_2 = [54.32, 'Строка' ]

print_params(b=25)
print_params(c=[1, 2, 3])
print_params()
print_params(10)
print_params('line', 5)
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)