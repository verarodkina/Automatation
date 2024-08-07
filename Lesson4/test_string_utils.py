import pytest
from string_utils import StringUtils

utils = StringUtils ()

"""capitalize"""


def test_capitalize ():
    """Pos"""
    assert utils.capitilize ("привет") == "Привет"
    assert utils.capitilize ("автоматизация сложна") == "Автоматизация сложна"
    assert utils.capitilize ("5673") == "5673"
    """Neg"""
    assert utils.capitilize ("  ") == "  "
    assert utils.capitilize ("") == ""
    assert utils.capitilize ("5673год") == "5673год"


"""trim"""

def trim ():
    assert utils.trim (" имя ") == "имя "
    """Neg"""
    assert utils.trim ("") == ""


@pytest.mark.xfail ()
def test_trim_number():
    assert utils.trim (5678) == "5678"

@pytest.mark.xfail ()
def test_trim_spaces():
    assert utils.trim (" имя ") == " имя "


"""to_list"""

@pytest.mark.parametrize('string, delimeter, result', [
    #Pos
    ("Григорий,Михаил,Аркадий", ",", ["Григорий", "Михаил", "Аркадий"]),
    ("7,8,9,10", ",", ["7", "8", "9", "10"]),
    ("*@$@%@&", "@", ["*", "$", "%", "&"]),
    #Neg
    ("", None, []),
    ("7,8,9,10", None, ["7", "8", "9", "10"]),
])
def test_to_list (string, delimeter, result):
    if delimeter is None:
        res = utils.to_list (string)
    else:
        res = utils.to_list (string, delimeter)
    assert res == result


"""contains"""

@pytest.mark.parametrize ('string, symbol, result', [
   ("красивый", "ы", True),
   (" питон", "н", True),
   ("усложнил ", "и", True),
   ("5678", "7", True),
   ("", "", True),
   ("Жизнь", "ж", False),
   ("мою", "5", False),
])
def test_contains (string, symbol, result):
    res = utils.contains (string, symbol)
    assert res == result


"""delete_symbol"""

@pytest.mark.parametrize ('string, symbol, result', [
    ("Лампа", "Л", "ампа"),
    ("медведь", "в", "медедь"),
    ("568", "6", "58",),
    ("дома хорошо", " ", "домахорошо"),
    ("стол ", " ", "стол"),
])
def test_elete_symbol (string, symbol, result):
    res = utils.delete_symbol (string, symbol)
    assert res == result

"""starts_with"""
@pytest.mark.parametrize ('string, symbol, result', [
    ("картина", "к", True),
    (" земля", " ", True),
    ("932", "9", True),
    ("Чертеж", "ч", False),
    ("матрица", " ", False),
    ("", "к", False),
])
def test_starts_with (string, symbol, result):
    res = utils.starts_with (string, symbol)
    assert res == result


"""end_wit"""
@pytest.mark.parametrize ('string, symbol, result', [
    ("мама", "а", True),
    ("красиво ", " ", True),
    ("329", "9", True),
    ("краски", "ч", False),
    ("кисти", " ", False),
    ("", "к", False),
])
def test_end_with (string, symbol, result):
    res = utils.end_with (string, symbol)
    assert res == result

"""is_empty"""
@pytest.mark.parametrize ('string, result', [
    ("", True),
    ("  ", True),
    ("        ", True),
    ("world", False),
    (" v ", False),
    ("444", False)
])
def test_is_empty (string, result):
    res = utils.is_empty (string)
    assert res == result

"""list_to_string""" 
@pytest.mark.parametrize ('lst, joiner, result', [ 
    (["Маша", "Гриша", "Таня"], ",", "Маша,Гриша,Таня"),
    (["жили", "были"], "-", "жили-были"),
    (["о", "к", "н", "о"], "", "окно"),
    ([], None, ""),
    ([], ",", ""),
    ([], "мама", "")
])
def test_list_to_string (lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string (lst)
    else:
        res = utils.list_to_string (lst, joiner)
    assert res == result 

