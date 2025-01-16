class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, name, start, stop, step=1):
        self.step = step
        if self.step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.name = name
        self.start = start
        self.stop = stop
        self.pointer = self.start
        self.control()

    def control(self):
        if (self.step > 0 and self.start >= self.stop) or (self.step < 0 and self.start <= self.stop):
            print(f'В {self.name} заданы неверные условия. Невозможно пройти от {self.start} до {self.stop} '
                  f'c шагом {self.step}. Проверьте!')

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration
        current_value = self.pointer
        self.pointer += self.step
        return current_value


try:
    iter1 = Iterator('Итераторе 1', 100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator('Итераторе 2', -5, 1)
iter3 = Iterator('Итераторе 3', 6, 15, 2)
iter4 = Iterator('Итераторе 4', 5, 1, -1)
iter5 = Iterator('Итераторе 5', 10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
