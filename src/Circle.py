from src.Figure import Figure

import math


class Circle(Figure):
    def __init__(self, ratio):
        self.ratio = ratio
        if not (str(self.ratio).isdigit()) or (self.ratio <= 0):
            raise ValueError('При задании радиуса круга введено не число или некорректное число')

    def perimeter(self):
        circle_perimeter = 2 * (math.pi * self.ratio)
        return circle_perimeter

    def area(self):
        circle_area = math.pi * (self.ratio ** 2)
        return circle_area
if __name__ == "__main__":
    circle1 = Circle(5)
    print(circle1.area())
    print(circle1.perimeter())