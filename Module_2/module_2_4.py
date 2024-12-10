import random

numbers = []
# numbers = [9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 99, 101]
for r_num in range(10):
    numbers.append(random.randint(1, 100))
# random.shuffle(numbers)

primes = []
not_primes = []

for i_num in numbers:
    is_prime = True
    for j_num in range(2, i_num // 2 + 1):
        if (i_num % j_num == 0):
            is_prime = False
            not_primes.append(i_num)
            break
    if is_prime == True and i_num != 1:
        primes.append(i_num)


print(f'Список: {numbers}')
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')
