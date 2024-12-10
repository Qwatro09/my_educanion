def print_params(a = 1, b = 'строка', c = True):
    print(f'\n {a}, {b}, {c}')


print_params()
print_params(b = 25, c = [1, 2, 3])

values_list = [101.99, 'Привет МИР', [1, 2, 3] ]
values_dict = {'a' : 1, 'b' : [4, 5, 6], 'c' : 'Hello world'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)