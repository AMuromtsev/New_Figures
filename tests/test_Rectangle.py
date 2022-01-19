

def test_square_area(rectangle_create):
    assert rectangle_create.area() == 100

def test_square_perimeter(rectangle_create):
    assert rectangle_create.perimeter() == 40

# Здесь можно было бы добавить ещё тест на add_area, но он работает в test_Square.py и test_Circle.py, нет смысда плодить одно и то же.