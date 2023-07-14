from classes.vacancies import Vacancy


class VacancyHH(Vacancy):
    """
    Экземпляр данного класса - это вакансия, полученная с платформы HeadHunter
    """

    def __init__(self, vacancies):
        self.__name_vacancies = vacancies['name']
        self.__id = vacancies['id']
        try:
            self.__salary_from = int(vacancies['salary']['from'])
        except TypeError:
            self.__salary_from = 0
        try:
            self.__salary_to = int(vacancies['salary']['to'])
        except TypeError:
            self.__salary_to = 0
        self.__experience = vacancies['experience']['name']
        self.__requirement = vacancies['snippet']['requirement']
        self.__vacancies_info = vacancies

    @property
    def name_vacancies(self):
        return self.__name_vacancies

    @property
    def id(self):
        return self.__id

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def experience(self):
        return self.__experience

    @property
    def requirement(self):
        return self.__requirement

    @property
    def vacancies_info(self):
        return self.__vacancies_info

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.__salary_to < other.__salary_to
