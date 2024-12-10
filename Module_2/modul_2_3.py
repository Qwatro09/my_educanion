my_list = [42, 69, 322, 13, 0, 99, 5, 9, 8, 7, 6, 5]

list_ind = 0

while list_ind <= len(my_list):
    list_ind += 1
    if list_ind >= len(my_list):
        break
    else:
        if my_list[list_ind] == 0:
            continue
        if my_list[list_ind] > 0:
            print(my_list[list_ind])
            continue
        if my_list[list_ind] < 0:
             break