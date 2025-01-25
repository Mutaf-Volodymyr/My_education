from calculator_1 import Calculator
import pytest



@pytest.fixture
def calculator():
    return Calculator()


@pytest.mark.sum_pos  # pytest -m sum_pos
def test_sum_positive_number(calculator):
    actual_result = calculator.sum(4, 5)
    expected_result = 9
    assert actual_result == expected_result


@pytest.mark.skip(reason="Тест не актуален")
def test_sum_negative_number(calculator):
    actual_result = calculator.sum(-10, -15)
    expected_result = -25
    assert actual_result == expected_result


@pytest.mark.xfail(reason='Может выдавать ошибки')
def test_sum_zeros(calculator):
    actual_result = calculator.sum(0, 0)
    expected_result = 0
    assert actual_result == expected_result


@pytest.mark.skipif(True, reason="Требуется Python 3.8 или выше")
def test_sum_float_number(calculator):
    actual_result = calculator.sum(0.1, 0.2)
    expected_result = 0.3
    assert actual_result == expected_result


# @pytest.mark.parametrize('a, b, expected_result',
#                          [
#                              (2, 5, 7),
#                              (0, 10, 10),
#                              (-2, 2, 0)
#                          ])
# def test_universal_for_sum(calculator, a, b, expected_result):
#     actual_result = calculator.sum(a, b)
#     assert actual_result == expected_result


@pytest.mark.parametrize('num1, num2, result', [
    (4, 5, 9),
    (-6, -10, -16),
    (-6, 6, 0),
    (5.61, 4.29, 9.9),
    (10, 0, 10)
])

def test_sum_positive_numbers(calculator, num1, num2, result):
    actual_result = calculator.sum(num1, num2)
    expected_result = result
    assert actual_result==expected_result


def test_average_positiv(calculator):
    actual_result = calculator.average(1, 2, 3, 4, 5)
    expected_result = 3
    assert actual_result==expected_result


def test_average_with_negtiv(calculator):
    actual_result = calculator.average(1, 2, 3, -4)
    expected_result = 0.5
    assert actual_result==expected_result

def test_average_empty(calculator):
    actual_result = calculator.average()
    expected_result = 0
    assert actual_result==expected_result




def test_len_gerland_1(calculator):
    actual_result = calculator.len_gerlanda([1,2,3,4,5])
    expected_result = 4
    assert actual_result == expected_result


def test_len_gerland_2(calculator):
    actual_result = calculator.len_gerlanda([1,4,2,3,5])
    expected_result = 8
    assert actual_result == expected_result


@pytest.mark.parametrize('nums, expected_result', [
    ([1,2,3,4,5], 4),
    ([1, 4, 2, 3, 5], 8),

])
def test_len_gerland_with_param(calculator, nums, expected_result):
    actual_result = calculator.len_gerlanda(nums)
    assert actual_result == expected_result