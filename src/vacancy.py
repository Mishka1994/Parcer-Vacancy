from abc import ABC, abstractmethod


class Vacancy(ABC):
    @abstractmethod
    def __init__(self):
        pass


class VacancyHeadHunter(Vacancy):
    """ Класс описывает экземпляры вакансий, полученных с сайта HeadHunter """

    def __init__(self, id_vacancy, name, url, salary, requirement, responsibility):
        """
        Инициализация экземпляра класса VacancyHeadHunter
        :param id_vacancy: индивидуальный ID вакансии
        :param name: название вакансии
        :param url: ссылка на вакансию
        :param salary: заработная плата
        :param requirement: требования
        :param responsibility: обязанности
        """
        self.id_vacancy = id_vacancy
        self.name = name
        self.url = url
        if salary is not None:
            self.salary = salary['from'] if salary['from'] is not None else salary['to']
        else:
            self.salary = 0
        self.requirement = requirement
        self.responsibility = responsibility

    @classmethod
    def init_item_hh(cls, data_obj):
        vacancy = VacancyHeadHunter(data_obj['id'], data_obj['name'], data_obj['url'], data_obj['salary'],
                                    data_obj['snippet']['requirement'], data_obj['snippet']['responsibility'])

        return vacancy

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id_vacancy}, {self.name}, {self.url}, {self.salary}," \
               f"{self.requirement}, {self.responsibility})"

    def __str__(self):
        return f"Класс: {self.__class__.__name__}, вакансия: {self.name}, id вакансии: {self.id_vacancy},\n" \
               f"ссылка: {self.url}, З/п: {self.salary},\n" \
               f"требования: {self.requirement}, обязанности: {self.responsibility}"

    def __lt__(self, other):
        if self.salary < other.salary:
            return True
        else:
            return False

    def __le__(self, other):
        if self.salary <= other.salary:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.salary > other.salary:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.salary >= other.salary:
            return True
        else:
            return False


class VacancySuperJob(Vacancy):
    """Класс описывает экземпляры вакансий, полученных с сайта SuperJob"""

    def __init__(self, id_vacancy, name, url, salary_from, salary_to, info_about_vacancy):
        """
        Инициализация экземпляра класса VacancySuperJob
        :param id_vacancy: индивидуальный ID вакансии
        :param name: название вакансии
        :param url: ссылка на вакансию
        :param salary_from: нижняя граница заработной платы
        :param salary_to: верхняя граница заработной платы
        :param info_about_vacancy: Информация о вакансии, содержащая требования и обязанности
        """
        self.id_vacancy = id_vacancy
        self.name = name
        self.url = url
        if salary_from == 0 and salary_to == 0:
            self.salary = 0
        self.salary = salary_from if salary_from != 0 else salary_to
        self.info = info_about_vacancy

    @classmethod
    def init_item_sj(cls, data_obj):
        """Инициализатор экземпляров"""
        vacancy = VacancySuperJob(data_obj['id'], data_obj['profession'], data_obj['link'], data_obj['payment_from'],
                                  data_obj['payment_to'], data_obj['candidat'])

        return vacancy

    def __repr__(self):
        """Информация об экземпляре для отладки"""
        return f"{self.__class__.__name__}({self.id_vacancy}, {self.name}, {self.url}, {self.salary}," \
               f"{self.info})"

    def __str__(self):
        """Информация об экземпляре для пользователя"""
        return f"Класс: {self.__class__.__name__}, id_вакансии: {self.id_vacancy}, название: {self.name},\n" \
               f"Ссылка: {self.url}, З/п: {self.salary}, требования и обязанности: {self.info} "

    def __lt__(self, other):
        if self.salary < other.salary:
            return True
        else:
            return False

    def __le__(self, other):
        if self.salary <= other.salary:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.salary > other.salary:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.salary >= other.salary:
            return True
        else:
            return False
