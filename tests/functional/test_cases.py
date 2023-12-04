from main import CalculateScore


def test_lack_of_frame():
    TEST_CASE = ""
    assert CalculateScore(TEST_CASE) == [
        "Invalid number of frames. There should be between 10 and 12 frames."
    ]


def test_much_of_frame():
    TEST_CASE = "53 72 52 33 21 54 x 52 63 x x x x"
    assert CalculateScore(TEST_CASE) == [
        "Invalid number of frames. There should be between 10 and 12 frames."
    ]


def test_bad_luck():
    TEST_CASE = "- - - - - - - - - -"
    assert CalculateScore(TEST_CASE) == 0


def test_full_strike():
    TEST_CASE = "x x x x x x x x x x x x"
    assert CalculateScore(TEST_CASE) == 300


def test_example():
    TEST_CASE = "53 72 x x 7/ 9/ 24 6/ x x x 5"
    assert CalculateScore(TEST_CASE) == 176


def test_example_2():
    TEST_CASE = "53 71 12 - 7/ 9/ 24 6/ 42 61"
    assert CalculateScore(TEST_CASE) == 83


def test_example_3():
    TEST_CASE = "- 5/ - x 52 9/ 24 6/ 2 1"
    assert CalculateScore(TEST_CASE) == 67


def test_example_4():
    TEST_CASE = "72 50 24 20 05 51 24 35 62 90"
    assert CalculateScore(TEST_CASE) == 64


# def test_invalid_frame():
#     TEST_CASE = "72 50 24 20 05 56 24 35 62 90"
#     assert CalculateScore(TEST_CASE) == 64
