import pytest
from Mk_Dir_Ya import make_dir,del_dir
from parameterized import parameterized


test_list = [
    ['11', True],
    ['11', False],
    ['KHGHJлорка', True],
]

@parameterized.expand(test_list)
def test_make_dir(dir_name, res):
    assert make_dir(dir_name) == res

@parameterized.expand(test_list)
def test_del_dir(dir_name, res):
    assert del_dir(dir_name) == res

