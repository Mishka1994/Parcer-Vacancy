import json
from abc import ABC, abstractmethod


class ProcessingData(ABC):
    """Абстрактный класс для наследования классами, которые обрабатывают данные,
    полученные от API сайтов с вакансиями """

    @abstractmethod
    def write_data(self, data):
        """Функция для записи данных в файл"""
        pass

    @abstractmethod
    def get_data(self):
        """Функция для получения данных из файла"""
        pass

    @abstractmethod
    def delete_data(self):
        """Функция для удаления данных из файла"""
        pass


class JSONFile(ProcessingData):
    """ Класс для работы с файлами, которые имеют расширение .json"""

    def write_data(self, data, file_with_vacancy='vacancy.json'):
        """
        Функция записывает данные в файл
        :param data: данные для записи
        :param file_with_vacancy: переменная хранит название файла для записи(по умолчанию 'vacancy.json')
        """
        with open(f"{file_with_vacancy}", "a+") as file:
            json.dump(data, indent=2, ensure_ascii=True, fp=file)

    def get_data(self, file_with_vacancy='vacancy.json'):
        """
        Функция считывает данные из указанного файла.
        :param file_with_vacancy: Содержит имя файла с данными.
        :return: возвращает словарь с данными
        """
        with open(f"{file_with_vacancy}") as file:
            object_with_data = json.load(file)
            return object_with_data

    def get_data_by_salary(self, salary, file_with_vacancy='vacancy.json'):
        """
        Функция для получения информации об вакансиях, с з/п, указанной пользователем
        :param salary: диапазон з/п для поиска.
        :param file_with_vacancy: имя файла для поиска данных.
        :return: возвращает словарь с результатом
        """
        # Список для хранения результатов
        result_list = []
        # Разбиваем переданный диапазон з/п на два числа для последующего сравнения
        list_salary = salary.split('-')
        # Получаем данные из файла
        obj_with_vacancies = self.get_data(file_with_vacancy)
        """
        Проверяем наличие ключей 'items' и 'objects'. 
        Первый ключ хранится в данных, полученных с сайта HeadHunter
        Второй ключ хранится в данных полученных с сайта SuperJob
        """
        # Проверяем наличие ключа 'items'
        if 'items' in obj_with_vacancies.keys():
            # перебираем список вакансий
            for element in obj_with_vacancies['items']:
                # Под ключом 'salary' могут находиться None значение, поэтому проверяем его наличие
                if element['salary'] is not None:
                    """
                    Если значение с ключом 'salary' не None, тогда проверяем,
                    содержат ли границы з/п None значения
                    """
                    if None in element['salary'].values():
                        # Если одно из значений None, то сразу сравниваем с оставшимся значением
                        if element['salary']['from'] is None:
                            if int(list_salary[0]) <= element['salary']['to'] <= int(list_salary[1]):
                                result_list.append(element)
                        if element['salary']['to'] is None:
                            if int(list_salary[0]) <= element['salary']['from'] <= int(list_salary[1]):
                                result_list.append(element)
                    else:
                        # Если оба значения не None, то из двух значений считаем среднее и сравниваем
                        # с заданным диапазоном з/п
                        average_salary = (element['salary']['from'] + element['salary']['to']) // 2
                        if int(list_salary[0]) <= average_salary <= int(list_salary[1]):
                            result_list.append(element)
        # Проверяем наличие ключа 'objects'
        elif 'objects' in obj_with_vacancies.keys():
            # Перебираем список вакансий
            for element in obj_with_vacancies['objects']:
                # Так же проверяем наличие None в значениях и при прохождении проверки складываем
                if element['payment_from'] is not None:
                    if int(list_salary[0]) <= element['payment_from'] <= int(list_salary[1]):
                        result_list.append(element)
                elif element['payment_to'] is not None:
                    if int(list_salary[0]) <= element['payment_to'] <= int(list_salary[1]):
                        result_list.append(element)
                else:
                    average_salary = (element['payment_from'] + element['payment_to'] // 2)
                    if int(list_salary[0]) <= average_salary <= list_salary[1]:
                        result_list.append(element)
        return result_list

    def delete_data(self, file_with_vacancy='vacancy.json'):
        """Функция удаляет все данные из файла"""
        with open(f'{file_with_vacancy}', "w") as file:
            file.write('')
            print("Данные удалены")
