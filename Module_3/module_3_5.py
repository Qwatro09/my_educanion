def get_multiplied_digits(number):
    if number % 10 == 0:
        number //= 10
    str_number = str(number)
    first = int(str_number[:1])
    if len(str_number) <= 1:
        return number
    else:
        number = first * get_multiplied_digits(int(str_number[1:]))
        return number


result = get_multiplied_digits(40203)

print(result)

result2 = get_multiplied_digits(402030)

print(result2)
