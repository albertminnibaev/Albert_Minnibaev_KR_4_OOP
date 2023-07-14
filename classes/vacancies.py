from abc import ABC, abstractmethod


class Vacancy(ABC):
    """
    Абстрактный класс для работы с вакансиями
    """

    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def name_vacancies(self):
        pass

    @abstractmethod
    def id(self):
        pass

    @abstractmethod
    def salary_from(self):
        pass

    @abstractmethod
    def salary_to(self):
        pass

    @abstractmethod
    def experience(self):
        pass

    @abstractmethod
    def requirement(self):
        pass

    @abstractmethod
    def vacancies_info(self):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass
