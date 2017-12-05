
import pytest
from expackage import my_add


def test_my_add():
    # Unit test for my_add function
    assert my_add(3, 2) == 5


def test_my_add_first_input_raises():
    # Test that my_add raises a TypeError when first input isn't a number
    with pytest.raises(TypeError) as excinfo:
        my_add('not a number', 5)
    error = 'Input to my_add should be either integers or floats'
    assert error == str(excinfo.value)


def test_my_add_second_input_raises():
    # Test that my_add raises a TypeError when second input isn't a number
    with pytest.raises(TypeError) as excinfo:
        my_add(2, 'not a number')
    error = 'Input to my_add should be either integers or floats'
    assert error == str(excinfo.value)
