import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda f, s: f == s, first, second))
print(result)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for my_elem in data_set:
                file.write(str(my_elem) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:

    def __init__(self, *worlds):
        self.worlds = worlds

    def __call__(self):
        return random.choice(self.worlds)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Забил гол!!', 'Пропустил гол')
print(first_ball())
print(first_ball())
print(first_ball())
