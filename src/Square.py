from src.Figure import Figure


class Square(Figure):
    def __init__(self, side):
        self.side = side  # Да, можно было в базовом классе создать список для сторон
        # и в каждом наследнике менять их количество, но мне лень :)
        if not (str(self.side).isdigit()) or (self.side <= 0):
            raise ValueError('При задании сторон фигуры введено не число или некорректное число')

    def area(self):
        square_area = self.side ** 2
        return square_area

    def perimeter(self):
        perimeter = self.side * 4
        return perimeter


if __name__ == "__main__":
    square1 = Square(10)
    print(square1.area())
