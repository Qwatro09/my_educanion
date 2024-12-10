def my_int(num):
    global total_sum
    total_sum += num
    return total_sum


def calculate_structure_sum(args):
    for i_elem in args:
        if isinstance(i_elem, (list, tuple, set)):
            calculate_structure_sum(i_elem)
        if isinstance(i_elem, dict):
            calculate_structure_sum(i_elem.items())
        if isinstance(i_elem, (int, float)):
            my_int(i_elem)
        if isinstance(i_elem, str):
            my_int(len(i_elem))


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_sum = 0

result = calculate_structure_sum(data_structure)

print(total_sum)
