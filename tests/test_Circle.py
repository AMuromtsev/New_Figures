def test_circle_area(circle_create):
    assert circle_create.area() == 78.53981633974483


def test_circle_perimeter(circle_create):
    assert circle_create.perimeter() == 31.41592653589793

def test_circle_add_area_Square(circle_create, square_create):
    assert circle_create.add_area(square_create) == 103.53981633974483