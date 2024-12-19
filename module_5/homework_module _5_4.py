class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.args = args
        cls.houses_history.append(cls.args[0])
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def __del__(self):
        print(f'{self.name}  снесён, но он останется в истории')
        return


h1 = House('ЖК Синее небо', 10)
print(House.houses_history)
h2 = House('ЖК Ближе к солнцу', 20)
print(House.houses_history)
h3 = House('ЖК Небоскреб', 45)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
