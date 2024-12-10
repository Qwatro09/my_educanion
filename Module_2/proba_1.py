import random

numbers = [9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 99, 101]

random.shuffle(numbers)

primes = []
not_primes = []
is_prime = True

for i_num in numbers:
    if i_num == 1:
        continue
    else:
        count = 0
        for j_num in range(2, int(i_num // 2 + 1)):
            if (i_num % j_num == 0):
                count += 1
                break
        if (count == 0):
            is_prime = True
        else:
            is_prime = False

        if is_prime is True:
            primes.append(i_num)
        else:
            not_primes.append(i_num)

print(f'Список: {numbers}')
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')