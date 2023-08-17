def test_vacancy_head_hunter(test_vacancy_hh1):
    assert test_vacancy_hh1.id_vacancy == '0123456'
    assert test_vacancy_hh1.name == "Backend-разработчик"
    assert test_vacancy_hh1.url == 'ссылка'
    assert test_vacancy_hh1.salary == 100000
    assert test_vacancy_hh1.requirement == 'Разработка и поддержка сайтов'
    assert test_vacancy_hh1.responsibility == 'Python, Django, SQL'


def test_vacancy_super_job(test_vacancy_sj1):
    assert test_vacancy_sj1.id_vacancy == '987654'
    assert test_vacancy_sj1.name == 'Frontend-разработчик'
    assert test_vacancy_sj1.url == 'ссылка_2'
    assert test_vacancy_sj1.salary == 100000
    assert test_vacancy_sj1.info == 'Frontend-разработчик с опытом от 3-х лет. Навык рисовать кнопочки приветствуется.'


def test_dunder_methods_hh(test_vacancy_hh1, test_vacancy_hh2):
    assert test_vacancy_hh1 > test_vacancy_hh2
    assert test_vacancy_hh2 < test_vacancy_hh1


def test_dunder_methods_sj(test_vacancy_sj1, test_vacancy_sj2):
    assert test_vacancy_sj1 < test_vacancy_sj2
    assert test_vacancy_sj2 > test_vacancy_sj1
