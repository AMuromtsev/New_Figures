import pytest
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Triangle import Triangle


@pytest.fixture
def square_create(request):
    test_square = Square(5)

    def teardown():
        print('Фикстура отработала')

    request.addfinalizer(teardown)
    return test_square


@pytest.fixture
def rectangle_create(request):
    test_rectangle = Rectangle(10, 10)

    def teardown():
        print('Фикстура отработала')

    request.addfinalizer(teardown)
    return test_rectangle


@pytest.fixture
def circle_create(request):
    test_circle = Circle(5)

    def teardown():
        print('Фикстура отработала')

    request.addfinalizer(teardown)
    return test_circle


@pytest.fixture
def triangle_create(request):
    test_triangle = Triangle(10, 10, 5)

    def teardown():
        print('Фикстура отработала')

    request.addfinalizer(teardown)
    return test_triangle
