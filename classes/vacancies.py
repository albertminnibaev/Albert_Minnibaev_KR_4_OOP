from abc import ABC, abstractmethod


class Vacancy(ABC):
    """
    Абстрактный класс для работы с вакансиями
    """

    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @property
    @abstractmethod
    def name_vacancies(self):
        pass

    @property
    @abstractmethod
    def id(self):
        pass

    @property
    @abstractmethod
    def salary_from(self):
        pass

    @property
    @abstractmethod
    def salary_to(self):
        pass

    @property
    @abstractmethod
    def experience(self):
        pass

    @property
    @abstractmethod
    def requirement(self):
        pass

    @property
    @abstractmethod
    def vacancies_info(self):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass
