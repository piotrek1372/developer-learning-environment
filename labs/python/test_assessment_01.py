import pytest
from assessment_01 import calculate_average

def test_average_of_three_numbers():
    result = calculate_average([2, 4, 6])

    assert result == 4.0

def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        calculate_average([])
