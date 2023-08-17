import json
from src.vacancy import VacancyHeadHunter
from src.fucnction_for_vacancies import top_vacancies, sorting_vacancies


def test_users_interface(test_file):
    with open(test_file) as file:
        result = json.load(file)
        result_list = [VacancyHeadHunter.init_item_hh(element) for element in result['items']]
        top_output = 5
        assert len(top_vacancies(result_list, top_output)) == top_output


def test_users_interface_index_error(test_file):
    with open(test_file) as file:
        result = json.load(file)
        result_list = [VacancyHeadHunter.init_item_hh(element) for element in result['items']]
        top_output = 100
        assert len(top_vacancies(result_list, top_output)) != top_output

