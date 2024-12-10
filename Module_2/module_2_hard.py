import random

num = random.randint(3, 20)
print(num)
result = ''

for i_num in range(1, num):
    for j_num in range(i_num, num):
        if i_num == j_num:
            continue
        else:
            if num % (i_num + j_num) == 0:
                result += str(i_num) + str(j_num)
print(result)