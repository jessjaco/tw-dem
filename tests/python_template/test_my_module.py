from python_template.my_module import square
from python_template.my_module import subtract


class TestSubtract:
    def test_subtract_positive(self):
        assert subtract(10, 5) == 5

    def test_subtract_negative(self):
        assert subtract(-5, -10) == 5

    def test_subtract_zero(self):
        assert subtract(0, 0) == 0


class TestSquare:
    def test_square_positive(self):
        assert square(4) == 16

    def test_square_negative(self):
        assert square(-3) == 9

    def test_square_zero(self):
        assert square(0) == 0
