import pathlib
import pytest

from pathlib import Path
from src.vacancy import VacancyHeadHunter, VacancySuperJob


@pytest.fixture()
def test_file():
    dir_path = pathlib.Path.cwd()
    test_file_path = Path(dir_path, 'test_vacancy.json')
    return test_file_path


@pytest.fixture()
def test_vacancy_hh1():
    return VacancyHeadHunter('0123456', 'Backend-разработчик', 'ссылка', {'from': None, 'to': 100000},
                             'Разработка и поддержка сайтов',
                             'Python, Django, SQL')


@pytest.fixture()
def test_vacancy_hh2():
    return VacancyHeadHunter('113471320', 'Q&A - тестировщик', 'ссылка_3', {'from': 30000, 'to': 60000},
                             'Тестирование приложений', 'Уметь тестировать приложения')


@pytest.fixture()
def test_vacancy_sj1():
    return VacancySuperJob('987654', 'Frontend-разработчик', 'ссылка_2',
                           0, 100000,
                           'Frontend-разработчик с опытом от 3-х лет. Навык рисовать кнопочки приветствуется.')


@pytest.fixture()
def test_vacancy_sj2():
    return VacancySuperJob('024681012', 'Middle-fullstack-разработчик', 'ссылка_4', 120000, 150000,
                           'Знание PHP, Python, SQL')
