import json

from pathlib import Path
from src.get_api_data import HeadHunterApi

from src.writing_data import JSONFile


def test_delete_data(test_file):
    test_item = JSONFile()
    test_item.delete_data(test_file)
    path = Path(test_file)
    is_empty = path.stat().st_size
    assert is_empty == 0


def test_write_data(test_file):
    key_wod = 'Python'
    test_item = JSONFile()
    hh_api = HeadHunterApi()
    result_request = hh_api.get_vacancies(key_wod)
    test_item.write_data(result_request, test_file)
    with open(test_file) as file:
        py_obj = json.load(file)
        assert len(py_obj) != 0


def test_get_data():
    test_item = JSONFile()
    result = test_item.get_data('test_vacancy.json')
    assert isinstance(result, dict)


def test_get_data_by_salary(test_file):
    test_item = JSONFile()
    pay_rate = '80000-120000'
    result = test_item.get_data_by_salary(pay_rate, test_file)
    assert result is not None
