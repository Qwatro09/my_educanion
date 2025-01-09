def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for i_num in numbers:
        try:
            result += i_num
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {i_num}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, str)):
            raise TypeError("В numbers записан некорректный тип данных")

        total_sum, incorrect_data_count = personal_sum(numbers)
        valid_count = len(numbers) - incorrect_data_count

        arithmetic_mean = total_sum / valid_count if valid_count > 0 else 0
    except ZeroDivisionError:
        return 0
    except TypeError as exc:
        print(exc)
        return None

    return arithmetic_mean


print(f'\nРезультат 1: {calculate_average("1, 2, 3")}\n')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}\n')
print(f'Результат 3: {calculate_average(567)}\n')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}\n')