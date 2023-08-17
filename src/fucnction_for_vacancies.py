def top_vacancies(list_with_vacancies, top):
    """
    Функция возвращает заданное пользователем количество объектов с информацией о вакансии.
    :param list_with_vacancies: Список с информацией о вакансиях.
    :param top: количество элементов для возврата.
    :return: Список нужной длины
    """
    list_for_top = []
    try:
        list_for_top = [elem for elem in list_with_vacancies[:top]]
    except IndexError:
        print(f"Длина списка({len(list_with_vacancies)}) меньше указанного количества вакансий({top})!")
    return list_for_top


def sorting_vacancies(list_with_vacancies):
    """Функция для сортировки вакансий по з/п """
    list_with_vacancies.sort(reverse=True)
    return list_with_vacancies
