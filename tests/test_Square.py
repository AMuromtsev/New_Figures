def test_square_area(square_create):
    assert square_create.area() == 25


def test_square_perimeter(square_create):
    assert square_create.perimeter() == 20


def test_square_add_area_rectangle(square_create, rectangle_create):
    assert square_create.add_area(rectangle_create) == 125