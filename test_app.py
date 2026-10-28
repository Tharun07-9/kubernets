from app import calculate_total, calculate_average

def test_calculate_total():
    assert calculate_total([80, 85, 90]) == 255

def test_calculate_average():
    assert calculate_average([80, 85, 90]) == 85.0
