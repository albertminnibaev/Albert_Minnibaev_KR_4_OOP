from abc import ABC, abstractmethod


class PlatformVacanciesApi(ABC):
    """
    Абстрактный класс для работы с API платформ с вакансиями
    """

    @property
    @abstractmethod
    def url(self):
        pass

    @property
    @abstractmethod
    def headers(self):
        pass

    @abstractmethod
    def get_vacancies(self, name_vacancies, filter_words):
        pass
