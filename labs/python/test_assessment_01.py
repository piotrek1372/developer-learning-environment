import pytest
from assessment_01 import calculate_average

@pytest.mark.parametrize(
        "numbers, expected",
        [
            ([2, 4, 6], 4.0),
            ([5], 5.0),
            ([1, 2], 1.5)
        ]
)

def test_average(numbers: list[int], expected: float):
    assert calculate_average(numbers) == expected

def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        calculate_average([])

def test_average_does_not_modify_input():
    numbers = [2, 4, 6]
    numbers_copy = numbers.copy()
    calculate_average(numbers)

    assert numbers == numbers_copy
