import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import difference  # Импорт функции difference из домашнего задания
from tests.constant_test_cases import PUBLIC_TEST_CASES, SECRET_TEST_CASES

ALL_TEST_CASES = PUBLIC_TEST_CASES + SECRET_TEST_CASES


def test_difference():
    for test_case in ALL_TEST_CASES:
        test_input1 = test_case.get("test_input1")
        test_input2 = test_case.get("test_input2")
        expected = test_case.get("expected")
        assert difference(test_input1, test_input2) == expected


test_difference()
