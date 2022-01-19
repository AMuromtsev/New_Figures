from src.Figure import Figure
import math

class Triangle(Figure):
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        if (not ((str(self.first_side).isdigit()))) or (not ((str(self.second_side).isdigit()))) or (
        not ((str(self.third_side).isdigit()))):
            raise ValueError('При задании сторон фигуры введено не число или некорректное число')
        if (self.first_side <= 0) or (self.second_side <= 0) or (self.third_side <= 0):
            raise ValueError('Введено отрицательное число или ноль')

    def perimeter(self):
        triangle_perimeter = self.first_side + self.second_side + self.third_side
        return triangle_perimeter

    def area(self):
        p = (self.perimeter()) / 2
        triangle_area = math.sqrt(
            p*((p - self.first_side) * (p - self.second_side) * (p - self.third_side)))
        return float(triangle_area)
    # здесь ещё могла бы быть проверка на корректность сторон треугольника, но её не будет :)


if __name__ == "__main__":
    triangle1 = Triangle(10, 10, 5)
    print(triangle1.area())
    print(triangle1.perimeter())
