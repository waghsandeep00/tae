# Assertions about expected exceptions
from math import e

import pytest


def test_excetion(name):
    if name != "Yana":
        raise Exception("Invalid User")
    else:
        print("Username is properly set")


def test_username_exception():
    """test that exception is raised for invalid username"""
    with pytest.raises(Exception):
        assert test_excetion("Yu")

    assert str(e.value) == "Username is properly set"


if __name__ == "__main__":
    pytest.main([__file__, "-k", "test_", "-v", "-s"])