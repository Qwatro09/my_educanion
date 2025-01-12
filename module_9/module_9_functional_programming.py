def apply_all_func(int_list, *functions):
    results = {}
    for fun in functions:
        answer = fun(int_list)
        results.update({fun.__name__: answer})
    return results


print(apply_all_func([6, 20, 15, 9], max, min), '\n')

print(apply_all_func([6, 20, 15, -5, 100, 9], len, sum, sorted))
