from src.Figure import Figure

class Rectangle(Figure):
    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side
        if (not ((str(self.first_side).isdigit())) or (not ((str(self.second_side).isdigit())))):
            raise ValueError('При задании сторон фигуры введено не число или некорректное число')
        if (self.first_side <= 0) or (self.second_side <= 0):  # разделил две проверки, чтобы было читабельно
            raise ValueError('Введено отрицательное число или ноль')

    def area(self):
        rectangle_area = self.first_side * self.second_side
        return rectangle_area

    def perimeter(self):
        rectangle_perimeter = (self.first_side + self.second_side) * 2
        return rectangle_perimeter


if __name__ == "__main__":
 pass