class Figure:
    def __init__(self):
        raise BaseException('Фигуру базового типа создать нельзя!!')


    def add_area(self, figure_name):
        self.figure_name = figure_name
        if isinstance(figure_name, Figure):
            added_area = self.area() + figure_name.area()
            return added_area
        else:
            raise ValueError('Передан неверный класс')
