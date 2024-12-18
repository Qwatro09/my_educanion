class House:
    def __init__(self, name, floors):
        self.name = name
        if isinstance(floors, int):
            self.number_of_floors = floors
        else:
            print(f'{floors} не может быть количеством этажей')
            exit()

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, other):
        self.number_of_floors = self.number_of_floors + other
        return self

    def __iadd__(self, other):
        self.number_of_floors += other
        return self

    def __radd__(self, other):
        self.number_of_floors = self.number_of_floors + other
        return self

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __str__(self):
        return f'\nНазвание: {self.name}, кол-во этажей: {self.number_of_floors}.'


h1 = House('ЖК Синее небо', 10)
h2 = House('ЖК Ближе к солнцу', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)

print(h1 >= h2)

print(h1 < h2)

print(h1 <= h2)

print(h1 != h2)