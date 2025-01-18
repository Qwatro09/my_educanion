def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        for j_num in range(2, int(num // 2) + 1):
            if num % j_num == 0:
                print('Составное')
                return num
        print('Простое')
        return num
    return wrapper

@is_prime
def sum_three(a, b, c):
    my_summ = a + b + c
    return my_summ

result = sum_three(2, 3, 6)
print(f'Сумма равна: {result}')
