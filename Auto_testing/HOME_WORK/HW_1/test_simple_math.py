from simple_math import SimpleMath
import pytest



@pytest.fixture
def simple_math():
    return SimpleMath()


@pytest.mark.parametrize('a, result', [
    (0, 0),
    (1, 1),
    (10, 100),
    (-3, 9)
])

def test_square(simple_math, a, result):
    actual_result = simple_math.square(a)
    expected_result = result
    assert actual_result==expected_result


@pytest.mark.parametrize('a, result', [
    (0, 0),
    (1, 1),
    (10, 1000),
    (-3, -27)
])
def test_cube(simple_math, a, result):
    actual_result = simple_math.cube(a)
    expected_result = result
    assert actual_result==expected_result