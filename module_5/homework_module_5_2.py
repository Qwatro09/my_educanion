class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floors):
        if new_floors > self.number_of_floors or new_floors < 1:
            print(f'Такого этажа не существует')
        else:
            for i_floors in range(1, new_floors + 1):
             print(i_floors)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.'



h1 = House('ЖК Синее небо', 10)
h2 = House('ЖК Ближе к солнцу', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))

# h1.go_to(5)
# h2.go_to(2)

# print(h1.name, h1.number_of_floors)
# print(h2.name, h2.number_of_floors)




# Пример выполняемого кода:
#
# h1 = House('ЖК Эльбрус', 10)
# # h2 = House('ЖК Акация', 20)
# #
# # __str__
#
# print(h1)
#
# print(h2)
#
#
#
# # __len__
#
#
#
#
#
# Вывод на консоль:
#
# Название: ЖК Эльбрус, кол-во этажей: 10
#
# Название: ЖК Акация, кол-во этажей: 20
#
# 10
#
# 20

