from src.vacancy import VacancyHeadHunter, VacancySuperJob
from src.get_api_data import HeadHunterApi, SuperJobApi
from src.writing_data import JSONFile
from src.fucnction_for_vacancies import top_vacancies, sorting_vacancies

# Ключевое слово для поиска вакансии
user_key_word = input("Введите ключевое слов для поиска: ")
# Количество вакансий выводимых на экран
count_vacancies = int(input("Введите ТОП вакансий для вывода: "))
# Выбор платформы для поиска вакансий
command = int(input("1: HeadHunter, 2: SuperJob\nВыберите платформу для поиска: "))
# Переменная для записи данных в файл и получения из файла
writer_data = JSONFile()
# Алгоритм действий при выборе платформы HeadHunter
if command == 1:
    hh_api = HeadHunterApi()
    # Получаем данные от API HeadHunter
    hh_vacancies = hh_api.get_vacancies(user_key_word)
    # Записываем данные в файл
    writer_data.write_data(hh_vacancies)
    # Вытаскиваем данные из файла
    list_data = writer_data.get_data()
    # Инициализируем список экземпляров класса VacancyHeadHunter
    list_vacancies = [VacancyHeadHunter.init_item_hh(element) for element in list_data['items']]
    # Сортируем список с вакансиями
    sorting_vacancies(list_vacancies)

    user_choose_output = input("Вывести указанный топ вакансий?(да/нет): ")
    if user_choose_output.lower() == "да":
        result = top_vacancies(list_vacancies, count_vacancies)
        for element in result:
            print(element)

    user_get_by_salary = input('Вывести вакансии по заданному диапазону з/п?(да/нет): ')
    if user_get_by_salary.lower() == 'да':
        # Получаем диапазон з/п от пользователя
        users_salary = input('Введите диапазон з/п:(число-число) ')
        # Получаем список вакансий, подходящих по з/п под заданный диапазон
        result = writer_data.get_data_by_salary(users_salary)
        for elem in result:
            print(elem)
# Алгоритм действий при выборе платформы SuperJob
elif command == 2:
    sj_api = SuperJobApi()
    # Получение данных с API SuperJob
    sj_vacancies = sj_api.get_vacancies(user_key_word)
    # Записываем данные в файл
    writer_data.write_data(sj_vacancies)
    # Получаем данные из файла
    list_data = writer_data.get_data()
    # Инициализируем список экземпляров класса VacancySuperJob
    list_vacancies = [VacancySuperJob.init_item_sj(element) for element in list_data['objects']]

    user_choose_output = input('Вывести указанный топ вакансий?(да/нет): ')
    if user_choose_output.lower() == 'да':
        result = top_vacancies(list_vacancies, count_vacancies)
        for element in result:
            print(element)

    user_get_salary_vacancies = input('Вывести вакансии по заданному диапазону з/п?(да/нет): ')
    if user_get_salary_vacancies.lower() == 'да':
        # Получаем диапазон з/п от пользователя
        users_salary = input('Введите диапазон з/п (число-число): ')
        # Получаем список вакансий, подходящих по з/п под заданный диапазон
        result = writer_data.get_data_by_salary(users_salary)
        for element in result:
            print(element)

writer_data.delete_data()
