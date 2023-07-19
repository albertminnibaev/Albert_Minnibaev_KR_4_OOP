from classes.platform_vacancies_api import PlatformVacanciesApi
import requests
import os

SuperJob_API_secret_key: str = os.getenv('SuperJob_API_secret_key')
SuperJob_API_access_token: str = os.getenv('SuperJob_API_access_token')


class SuperJobAPI(PlatformVacanciesApi):
    """
    Класс для получения вакансий от платформы SuperJobAPI по API
    """

    @property
    def url(self):
        return 'https://api.superjob.ru/2.0/vacancies/'

    @property
    def headers(self):
        return {
            'ID': '2743',
            'X-Api-App-Id': SuperJob_API_secret_key,
            'Authorization': f'Bearer r.000000010000001.example.{SuperJob_API_access_token}',
        }

    def get_vacancies(self, name_vacancies, filter_words):
        data = {}
        params = {
            'keywords': [(1, 'or', name_vacancies), (10, 'or', filter_words)],
            'offset': 0,
            'limit': 1000,
        }
        try:
            req = requests.get(self.url, params=params, headers=self.headers)
        except requests.ConnectionError as e:
            print("Ошибка подключения:", e)
        except requests.Timeout as e:
            print("Ошибка тайм-аута:", e)
        except requests.RequestException as e:
            print("Ошибка запроса:", e)
        else:
            data = req.json()
            return data
        return data
