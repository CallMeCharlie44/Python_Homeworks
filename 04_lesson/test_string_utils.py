import pytest
from string_utils import StringUtils


string_utils = StringUtils()


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


    import pytest
from string_utils import StringUtils

utils = StringUtils()


# --- trim ---
@pytest.mark.parametrize("input_str, expected", [
    ("  hello  ", "hello"),  # пробелы по краям
    ("noSpaces", "noSpaces"),  # без изменений
    ("   ", ""),  # только пробелы
    ("", ""),  # пустая строка
    (None, None)  # негатив — None
])
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected


# --- to_list ---
@pytest.mark.parametrize("input_str, delimiter, expected", [
    ("a,b,c", ",", ["a", "b", "c"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),  # пустая строка
    (None, ",", []),  # негатив - None
    ("abc", None, ["abc"])  # нет разделителя → возвращаем всю строку списком?
])
def test_to_list(input_str, delimiter, expected):
    if delimiter is None:
        # Функция упадёт без проверки, поэтому защищаем тест
        with pytest.raises(TypeError):
            utils.to_list(input_str, delimiter)
    else:
        assert utils.to_list(input_str, delimiter) == expected


# --- contains ---
@pytest.mark.parametrize("string, symbol, expected", [
    ("Hello", "H", True),
    ("Hello", "o", True),
    ("Hello", "z", False),
    ("", "H", False),  # пустая строка
    ("Hello", "", False),  # пустой символ
    (None, "a", False),  # негатив — None
])
def test_contains(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


# --- delete_symbol ---
@pytest.mark.parametrize("string, symbol, expected", [
    ("banana", "a", "bnn"),
    ("banana", "x", "banana"),  # нет символа
    ("", "a", ""),  # пустая строка
    (None, "a", None),  # негатив
    ("test", "", "test"),  # пустой символ → без изменений
])
def test_delete_symbol(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


# --- starts_with ---
@pytest.mark.parametrize("string, symbol, expected", [
    ("Python", "P", True),
    ("Python", "x", False),
    ("", "a", False),
    ("Python", "", False),
    (None, "P", False),
])
def test_starts_with(string, symbol, expected):
    assert utils.starts_with(string, symbol) == expected


# --- end_with ---
@pytest.mark.parametrize("string, symbol, expected", [
    ("hello", "o", True),
    ("hello", "x", False),
    ("", "x", False),
    ("hello", "", False),
    (None, "o", False),
])
def test_end_with(string, symbol, expected):
    assert utils.end_with(string, symbol) == expected


# --- is_empty ---
@pytest.mark.parametrize("string, expected", [
    ("", True),
    (None, True),
    (" ", False),  # пробел = не пусто!
    ("text", False),
])
def test_is_empty(string, expected):
    assert utils.is_empty(string) == expected


# --- list_to_string ---
@pytest.mark.parametrize("lst, joiner, expected", [
    (["a", "b", "c"], ",", "a,b,c"),
    (["1", "2"], "-", "1-2"),
    ([], ",", ""),  # пустой список
])
def test_list_to_string(lst, joiner, expected):
    assert utils.list_to_string(lst, joiner) == expected