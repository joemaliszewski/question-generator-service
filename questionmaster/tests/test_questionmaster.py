"""Tests for `questionmaster` package."""

import pytest
from assertpy import assert_that

from questionmaster.questionmaster import func, Class


@pytest.mark.parametrize(
    "a, b, expected",
    [
        # Test with range of expected inputs
        (1, "foo", ["foo"]),
        (1, "bar", ["bar"]),
    ],
)
def test_function_works(a, b, expected):
    """Single line description of what this unit test is trying to do."""
    result = func(a, b)
    assert_that(result).is_equal_to(expected)


@pytest.mark.parametrize("a, b, err_msg", [(2, "foo", "'a' must be equal to '1'")])
def test_function_raises_exception(a, b, err_msg):
    """Test that the error message is raised with invalid inputs"""
    with pytest.raises(Exception) as e_info:
        func(a, b)
        assert_that(err_msg).is_equal_to(e_info.value)


def test_class_init():
    """Test that the class is instantiated correctly"""
    c = Class()
    assert_that(c.ham).is_equal_to(False)
    assert_that(c.eggs).is_equal_to(0)
