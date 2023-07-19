from classes.platform_vacancies_api import PlatformVacanciesApi
import requests


class HeadHunterAPI(PlatformVacanciesApi):
    """
    Класс для получения вакансий от платформы HeadHunter по API
    """

    @property
    def url(self):
        return 'https://api.hh.ru/vacancies'

    @property
    def headers(self):
        return {}

    def get_vacancies(self, name_vacancies, filter_words):
        data = {}
        params = {
            'text': f'NAME:{name_vacancies}',  # Текст фильтра. В имени должно быть слово "python"
            'page': 1,  # Индекс страницы поиска на НН
            'per_page': 100,  # Кол-во вакансий на 1 странице
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
