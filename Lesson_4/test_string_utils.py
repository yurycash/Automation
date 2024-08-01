import pytest
from string_utils import StringUtils

utils = StringUtils()

"""CAPITALIZE"""
"""var 1"""


def test_capitalize():
    """POSITIVE"""
    assert utils.capitilize("yury") == "Yury"
    assert utils.capitilize("ростов") == "Ростов"
    assert utils.capitilize("hi!") == "Hi!"
    """NEGATIVE"""
    assert utils.capitilize("     ") == "     "
    assert utils.capitilize("123") == "123"


"""var 2"""


@pytest.mark.parametrize("input_string, expected_output", [
   ("yury", "Yury"),
   ("ростов", "Ростов"),
   ("hi!", "Hi!"),
   ("     ", "     "),
   ("123test", "123test")
])
def test_capitalize(input_string, expected_output):
    assert utils.capitilize(input_string)


"""TRIM"""


def test_trim():
    """POSITIVE"""
    assert utils.trim(" Yury") == "Yury"
    assert utils.trim(" Yury ") == "Yury "
    assert utils.trim(" Hello world ") == "Hello world "
    """NEGATIVE"""
    assert utils.trim("") == ""
    assert utils.trim("46746") == "46746"


@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(46746) == "46746"


@pytest.mark.xfail()
def test_trim_with_spases_output():
    assert utils.trim(" Привет! ") == " Привет! "


"""TO LIST"""


@pytest.mark.parametrize('string, delimeter, result', [
    # POSITIVE
    ("Собака,Кошка,Мышь", ",", ["Собака", "Кошка", "Мышь"]),
    ("1-2-3-4-5", "-", ["1", "2", "3", "4", "5"]),
    ("Rock N Roll", " ", ["Rock", "N", "Roll"]),
    # NEGATIVE
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


"""contains"""


@pytest.mark.parametrize('string, symbol, result', [

    ("Ростов", "Р", True),
    ("Yury ", "y", True),
    (" вагон", " ", True),
    ("", "", True),
    ("Салтыков-Щедрин", "-", True),
    ("789", "8", True),

    ("Rim", "r", False),
    ("", "1", False),
    ("Hello", "Ж", False),
    ("A", "А", False),
    ("456", "M", False),

])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


"""delete_symbol"""


@pytest.mark.parametrize('string, symbol, result', [

    ("Ростов", "Р", "остов"),
    ("Yury", "y", "Yur"),
    (" вагон", " ", "вагон"),
    ("", "", ""),
    ("Салтыков-Щедрин", "-", "СалтыковЩедрин"),
    ("789", "8", "79"),

    ("Rim", "r", "Rim"),
    ("", "1", ""),
    ("Hello", "Ж", "Hello"),
    ("456", "M", "456"),
    ("Sky", "r", "Sky"),
    ("Rim", "", "Rim"),

])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


"""starts_with"""


@pytest.mark.parametrize('string, symbol, result', [

    ("Ростов", "Р", True),
    ("Yury ", "Y", True),
    (" вагон", " ", True),
    ("", "", True),
    ("Салтыков-Щедрин", "с", False),
    ("789", " ", False),
    ("Rim", "r", False),
    ("", "1", False),
    ("Hello", "Ж", False),
    ("A", "А", False),
    ("456", "M", False),

])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


"""end_with"""


@pytest.mark.parametrize('string, symbol, result', [

    ("Ростов", "в", True),
    ("Yury", "y", True),
    ("вагон ", " ", True),
    ("", "", True),
    ("456", "6", True),

    ("789", " ", False),
    ("Rim", "r", False),
    ("", "1", False),
    ("Hello", "Ж", False),
    ("A", "А", False),
    ("456", "M", False),

])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


"""is_empty"""


@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),
    ("  ", True),
    ("торт", False),
    ("торт с пробелом)", False),
    ("654", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


"""list_to_string"""


@pytest.mark.parametrize('lst, joiner, result', [

    (["Rock", "Roll"], "-N-", "Rock-N-Roll"),
    ([1, 2, 3, 4], None, "1, 2, 3, 4"),
    (["S", "K", "Y"], "", "SKY"),
    (["", "", ""], " ", "  "),

    ([], "12test1", ""),
    ([], None, ""),
    ([], ",", "")

])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result
