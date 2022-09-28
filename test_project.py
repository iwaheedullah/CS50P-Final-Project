from project import get_length, fetch_data, print_blanks
import pytest


# Test length of country name.
def test_get_length():
    assert get_length("pakistan") == 8


def test_get_length2():
    assert get_length("india") == 5


# Test status of response data.
def test_response_code():
    with pytest.raises(SystemExit):
        fetch_data("https://restcountries.com/v3.1/")


def test_response_code2():
    with pytest.raises(SystemExit):
        fetch_data("https://restcountries.com/all")


# Test dashes.
def test_dashes():
    assert print_blanks(5) == ["_", "_", "_", "_", "_"]


def test_dashes2():
    assert print_blanks(7) == ["_", "_", "_", "_", "_", "_", "_"]