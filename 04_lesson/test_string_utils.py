import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# Ужк созданные тесты в фале. Не мои

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


#Тесты на 2-ю функцию. Удаление пробелов

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [ 
    ("  Пробелы? ", "Пробелы?"),
    ("Пробелы", "Пробелы"),
])
def test_trim_posotove(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [ 
    ("Пробелы    ", "Пробелы"),
    (None, None),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


#Тесты на 3-ю функцию с искомым символом

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Привет", "П", True),
    ("Чарльз Леклееер", "М", False ),
])
def test_symbol_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

# Тест на функцию Raises
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Out of touch", "", ValueError),
])
def test_symbol_positive(input_str, symbol, expected):
    with pytest.raises(ValueError):
        string_utils.contains(input_str, symbol)

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    (" ", "П", True),
    ("Чарльз", "", False ),
])
def test_symbol_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# Тест на 4-ую функцию. Удаление символов

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Удалить_работу", "_", "Удалитьработу"),
    ("ProMax", "Max", "Pro"),
])
def test_delite_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("  ", "", ""),
    ("Delete", "", "Delete"),
])
def test_delite_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected   
