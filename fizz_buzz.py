import pytest


# Production Code
def fizz_buzz(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):  # Nested if statement similar to AND function
            return "FizzBuzz"
        return "Fizz"
    if is_multiple(value, 5):
        return "Buzz"
    return str(value)


def is_multiple(value, by):
    return (value % by) == 0


def check_fizz_buzz(value, exp_value):
    ret_val = fizz_buzz(value)
    assert ret_val == exp_value


def test_returns1_with_1_pass_in():
    check_fizz_buzz(1, "1")


def test_returns2_with_2_pass_in():
    check_fizz_buzz(2, "2")


def test_returns_fizz_3_pass_in():
    check_fizz_buzz(3, "Fizz")


def test_returns_buzz_5_pass_in():
    check_fizz_buzz(5, "Buzz")


def test_returns_fizz_multiples3_6_pass_in():
    check_fizz_buzz(6, "Fizz")


def test_returns_buzz_multiples5_10_pass_in():
    check_fizz_buzz(10, "Buzz")


def test_returns_fizzbuzz_multiples_15_pass_in():
    check_fizz_buzz(15, "FizzBuzz")
