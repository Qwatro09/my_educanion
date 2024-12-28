import math


class Figure:
    sides_count = 0

    def __init__(self, color=(255, 255, 255), *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= g <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return (all(side > 0 for side in new_sides)
                and len(new_sides) == self.sides_count)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
            return True
        return False


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(255, 255, 255), length_circle=1):
        super().__init__(color, length_circle)
        self.__radius = length_circle / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(255, 255, 255), *sides):
        super().__init__(color, *sides)

    def get_square(self):
        s = sum(self.__sides) / 2
        return math.sqrt(s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(255, 255, 255), edge_length=1):
        super().__init__(color)
        self.set_sides(*[edge_length] * self.sides_count)

    def get_volume(self):
        edge_length = self.get_sides()[0]
        return edge_length ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())