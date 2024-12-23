class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.model = __model
        self.engine_power = __engine_power
        self.color = __color.lower()

    def get_model(self):
        return f'Модель: {self.model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.engine_power}'

    def get_color(self):
        return f'Цвет: {self.color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()