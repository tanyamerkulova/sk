import pytest
from string_utils import StringUtils


@pytest.mark.parametrize('input_str, result', [
    ("skypro", "Skypro"),
    ("Skypro", "Skypro"),
    ("SKYPRO", "SKYPRO"),
    (" ", " "),
    ("", ""),
    ("Sky Pro", "Sky Pro"),
    ("sky pro", "Sky pro"),
    ("123skypro", "123skypro")
    ])
def test_capitalize(input_str, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(input_str)
    assert res == result


@pytest.mark.parametrize('input_str, result', [
    ("   skypro", "skypro"),
    (" Skypro", "Skypro"),
    (" SKYPRO", "SKYPRO"),
    ("skypro", "skypro"),
    (" ", ""),
    ("", ""),
    (" Sky Pro", "Sky Pro"),
    ("     sk y pro", "sk y pro")
    ])
def test_trim(input_str, result):
    string_utils = StringUtils()
    res = string_utils.trim(input_str)
    assert res == result


@pytest.mark.parametrize('input_str, symbol, result', [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("Skypro", "U", False),
    ("SkyPro", "Sky", True),
    ("Sky Pro", " ", True),
    ("", "a", False),
    ("SkyPro", "Y", False),
    ("Skypro", "", True)
    ])
def test_contains(input_str, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(input_str, symbol)
    assert res == result


@pytest.mark.parametrize('input_str, symbol, result', [
    ("SkyPro", "k", "SyPro"),
    ("colour", "o", "clur"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "XYZ", "SkyPro"),
    ("", "S", ""),
    ("", "", ""),
    ("sss", "s", ""),
    ("SkyPro", "s", "SkyPro"),
    ("Sky Pro", " ", "SkyPro")
    ])
def test_delete_symbol(input_str, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input_str, symbol)
    assert res == result
