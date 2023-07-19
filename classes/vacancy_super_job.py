from classes.vacancies import Vacancy


class VacancySuperJob(Vacancy):
    """
    Экземпляр данного класса - это вакансия, полученная с платформы SuperJob
    Экземпляр класса инициализируется содержимым из словаря, полученного с платформы SuperJob и
     должен иметь обязательные приватные свойства:
    '__name_vacancies' - название вакансии
    '__id' - id номер вакансии
    '__salary_from' - нижний порог по зарплате, при отсутствии информации в вакансии присваивается 0
    '__salary_to' - верхняя граница по зарплате, при отсутствии информации в вакансии присваивается 0
    '__experience' - опыт работы
    '__requirement' - требования к соискателю
    '__vacancies_info' - словарь с полной информацией по вокансии
    """

    __slots__ = ['__name_vacancies', '__id', '__salary_from', '__salary_to',
                 '__experience', '__requirement', '__vacancies_info']

    def __init__(self, vacancies):
        self.__name_vacancies = vacancies['profession']
        self.__id = vacancies['id']
        try:
            self.__salary_from = int(vacancies['payment_from'])
        except TypeError:
            self.__salary_from = 0
        try:
            self.__salary_to = int(vacancies['payment_to'])
        except TypeError:
            self.__salary_to = 0
        self.__experience = vacancies['experience']["title"]
        self.__requirement = vacancies['candidat']
        self.__vacancies_info = vacancies

    def __str__(self):
        return f"Название вакансии: {self.__name_vacancies}\n" \
               f"зарплата: от {self.__salary_from} до {self.__salary_to}\n" \
               f"опыт: {self.__experience}\n" \
               f"требования: {self.__requirement}"

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
