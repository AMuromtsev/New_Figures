def test_triangle_area(triangle_create):
    assert triangle_create.area() == 24.206145913796355

def test_triangle_perimeter(triangle_create):
    assert triangle_create.perimeter() == 25


 # Здесь можно было бы добавить ещё тест на add_area, но он работает в test_Square.py и test_Circle.py, нет смысда плодить одно и то же.