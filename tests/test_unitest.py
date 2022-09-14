import unittest
from main import get_name_in_number, get_num_shelf_in_num, add_shelf, del_doc
from parameterized import parameterized


class TestFuntion(unittest.TestCase):
    # def setUp(self) -> None:
    #     print('Start')
    #
    # def tearDown(self) -> None:
    #     print('Stop')

    @parameterized.expand(
        [
            ["2207 876234", "Василий Гупкин"],
            ["11-2", "Геннадий Покемонов"],
            ["10006", "Аристарх Павлов"],
            ['555', 'Номер не найден']
        ]
    )
    def test_get_name_in_number(self, number_, result):
        calc_result = get_name_in_number(number_)
        self.assertEqual(calc_result, result)


    @parameterized.expand(
        [
            ['2207 876234', '1'],
            ['10006', '2']
        ]
    )
    def test_get_num_shelf_in_num(self, num_doc, num_shelf):
        calc_result = get_num_shelf_in_num(num_doc)
        self.assertEqual(calc_result, num_shelf)

    @parameterized.expand(
        [
            ['567', True],
            ['2', False]
        ]
    )
    def test_add_shelf(self, num_shelf, res):
        calc_result = add_shelf(num_shelf)
        self.assertEqual(calc_result, res)

    @parameterized.expand(
        [
            ['2207 876234', True],
            ['11-2', True],
            ['5455 02876', False]
        ]
    )
    def tests_del_doc(self, num_doc, res):
        calc_res = del_doc(num_doc)
        self.assertEqual(calc_res, res)
