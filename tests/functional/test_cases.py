from main import CalculateScore2


def test_no_input():
    TEST_CASE_2 = ""
    assert CalculateScore2(TEST_CASE_2) == ['The length of the input not valid. The frames must be between 10 and 12.']


def test_full_strike():
    TEST_CASE = 'x x x x x x x x x x x x'
    assert CalculateScore2(TEST_CASE) == 300

def test_example():
    TEST_CASE_2 = "53 72 x x 7/ 9/ 24 6/ x x x 5"
    assert CalculateScore2(TEST_CASE_2) == 176