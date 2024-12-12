class House():
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floors):
        if new_floors > self.number_of_floors or new_floors < 1:
            print(f'Такого этажа не существует')
        else:
            for i_floors in range(1, new_floors + 1):
                print(i_floors)


h1 = House('ЖК Синее небо', 40)
h2 = House('Хуторок', 2)

h1.go_to(45)
h2.go_to(2)

# print(h1.name, h1.number_of_floors)
# print(h2.name, h2.number_of_floors)

