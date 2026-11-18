from p5 import calculate_si

def test_simple_interest():
    assert calculate_si(10000, 5, 2) == 1000

def test_zero_interest():
    assert calculate_si(10000, 0, 2) == 0

def test_one_year():
    assert calculate_si(5000, 10, 1) == 500