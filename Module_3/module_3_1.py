calls = 0


def count_calls():
    # counter = 0
    global calls
    # counter += 1
    calls += 1


def string_info(my_string):
    count_calls()
    tuple_info = (len(my_string), my_string.upper(), my_string.lower())
    return tuple_info


def is_contains(string, list_to_search):
    count_calls()
    for i_num in list_to_search:
        # my_flag = False
        if string.lower() == i_num.lower():
            # my_flag = True
            # break
            return  True
    # if my_flag == True:
    #     return True
    # else:
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Hello world'))
print(is_contains('Urban', ['ban', 'BaNaN', 'URban']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('hello', ['world', 'Hello']))
print(is_contains('Привет', ['мир', 'пока']))
print(calls)
