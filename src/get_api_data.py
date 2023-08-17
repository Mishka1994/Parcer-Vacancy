import os
import requests
import json

from abc import ABC, abstractmethod


class DateApi(ABC):
    """Абстрактный класс для получения данных с сайта по API"""
    @abstractmethod
    def get_vacancies(self, key_word):
        """Метод получающий данные через API """
        pass


class HeadHunterApi(DateApi):
    """Класс получающий данные с сайта HeadHunter через API"""
    def get_vacancies(self, key_word):
        """
        Метод дял получения данных с сайта HeadHunter
        :param key_word: Ключевое слов для поиска
        :return: словарь Python
        """
        headers = 'User-Agent: MyApp/1.0 (my-app-feedback@example.com)'
        options = {"page": 1,
                   "pages": 50,
                   "per_page": 5,
                   "text": f"{key_word}"
                   }
        answer = requests.get('https://api.hh.ru/vacancies/',  params=options)
        print(answer.text)
        data = answer.content.decode()
        py_obj = json.loads(data)

        return py_obj


class SuperJobApi(DateApi):
    """Класс получающий данные с сайта SuperJob через API"""
    api_key = os.getenv("SUPER_JOB_API")

    def get_vacancies(self, key_word):
        """
        Метод для получения данных с сайта SuperJob через API
        :param key_word: Ключевое слово для поиска
        :return: словарь Python
        """
        options = {
            "keyword": key_word,
            "page": 1,
            "count": 10,

        }
        my_api = {"X-Api-App-Id": SuperJobApi.api_key}
        answer = requests.get(f"https://api.superjob.ru/2.0/vacancies/",
                              headers=my_api,
                              params=options)
        data = answer.content.decode()
        py_obj = json.loads(data)
        return py_obj


