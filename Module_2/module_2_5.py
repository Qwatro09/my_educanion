# В случае передачи аргумента со значением 0 или меньше, будет возвращаться пустой список.

def get_matrix(n, m, value):
    matrix = []

    if n <= 0 or m <= 0 or value <= 0:
        return matrix
    else:
        for i_num in range(n):
            list_1 = []
            matrix.append(list_1)
            for j_num in range(m):
                list_1.append(value)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)