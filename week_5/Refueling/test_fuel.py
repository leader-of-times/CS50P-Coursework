from fuel import convert, gauge
from pytest import raises

def main():
    test_convert_valid_fraction()
    test_convert_invalid_format()
    test_convert_division_by_zero()
    test_convert_x_greater_than_y()
    test_gauge_less_than_or_equal_to_1()
    test_gauge_greater_than_or_equal_to_99()
    test_gauge_between_1_and_99()

def test_convert_valid_fraction():
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_convert_invalid_format():
    with raises(ValueError):
        convert("3.5/4")
    with raises(ValueError):
        convert("3/4.5")

def test_convert_division_by_zero():
    with raises(ZeroDivisionError):
        convert("3/0")

def test_convert_x_greater_than_y():
    with raises(ValueError):
        convert("5/3")

def test_gauge_less_than_or_equal_to_1():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_greater_than_or_equal_to_99():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_between_1_and_99():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"

if __name__ == "__main__":
    main()
