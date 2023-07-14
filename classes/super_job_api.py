from classes.platform_vacancies_api import PlatformVacanciesApi
import requests


class SuperJobAPI(PlatformVacanciesApi):
    """
    Класс для получения вакансий от платформы SuperJobAPI по API
    """

    __api_sj = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self, name_vacancies, filter_words):
        params = {
            'keywords': [(1, 'or', name_vacancies), (10, 'or', filter_words)],
            'town': "Москва",  # Поиск осуществляется по вакансиям города Москва
            'period': 7,
        }
        headers = {
            'ID': '2743',
            'X-Api-App-Id': 'v3.r.14969054.17de73f28457f21470538f0ea911bca72606e6b8.2ef2df5ef10274581a1d19a930ad4cbc4a3a5e09',
            'Authorization': 'Bearer r.000000010000001.example.v3.r.14969054.666f3ffef8663b6c046516386d5444b167365c3f.b4e86410b77f7572981dff564224b3bca4907015',
        }
        req = requests.get('https://api.superjob.ru/2.0/vacancies', params=params, headers=headers)
        data = req.json()
        return data
