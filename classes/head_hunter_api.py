from classes.platform_vacancies_api import PlatformVacanciesApi
import requests


class HeadHunterAPI(PlatformVacanciesApi):
    """
    Класс для получения вакансий от платформы HeadHunter по API
    """

    __api_hh = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, name_vacancies, filter_words):
        params = {
            'text': f'NAME:{name_vacancies}',  # Текст фильтра. В имени должно быть слово "python"
            'area': 1,  # Поиск осуществляется по вакансиям города Москва
            'page': 1,  # Индекс страницы поиска на НН
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        req = requests.get(self.__api_hh, params=params)
        data = req.json()
        return data
