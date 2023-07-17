from classes.platform_vacancies_api import PlatformVacanciesApi
import requests
import os

SuperJob_API_secret_key: str = os.getenv('SuperJob_API_secret_key')
SuperJob_API_access_token: str = os.getenv('SuperJob_API_access_token')


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
            'X-Api-App-Id': SuperJob_API_secret_key,
            'Authorization': f'Bearer r.000000010000001.example.{SuperJob_API_access_token}',
        }
        req = requests.get('https://api.superjob.ru/2.0/vacancies', params=params, headers=headers)
        data = req.json()
        return data
