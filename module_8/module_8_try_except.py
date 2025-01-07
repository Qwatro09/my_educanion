def add_everything_up(number, my_str):
    try:
        result = number + my_str
    except TypeError as exc:
        print(f'Из-за сложения разных типов данных получили ошибку: {exc} с аргументом {exc.args}')
        print('И тем не менее вот ответ, в виде строкового представления этих двух данных вместе: ', end='')
        return str(number) + str(my_str)
    else:
        print(f'Переданы числа {number} и {my_str}. Их сумма = ', end='')
        return round(result, 3)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
