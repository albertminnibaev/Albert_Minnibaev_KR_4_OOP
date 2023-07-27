class InitFromHH:
    """
    Класс Mixin, используется для создания экземпляров класса Vacancy, используя при инициализации
    информацию, полученную с платформы HeadHunter.
    """

    @staticmethod
    def init_from_hh_dict(data_from_hh):
        name = data_from_hh['name'] # название вакансии
        id = data_from_hh['id'] # id номер вакансии
        try:
            salary_from = int(data_from_hh['salary']['from']) # нижний порог по зарплате, при отсутствии информации в вакансии присваивается 0
        except TypeError:
            salary_from = 0
        try:
            salary_to = int(data_from_hh['salary']['to']) # верхняя граница по зарплате, при отсутствии информации в вакансии присваивается 0
        except TypeError:
            salary_to = 0
        experience = data_from_hh['experience']['name'] # опыт работы
        requirement = data_from_hh['snippet']['requirement'] # требования к соискателю
        vacancies_info = data_from_hh # словарь с полной информацией по вокансии
        url = "https://hh.ru/" # информация о сайте с вакансией

        instance = Vacancy(name, id, salary_from, salary_to, experience, requirement, vacancies_info, url)
        return instance


class InitFromSJ:
    """
    Класс Mixin, используется для создания экземпляров класса Vacancy, используя при инициализации
    информацию, полученную с платформы SuperJob.
    """

    @staticmethod
    def init_from_sj_dict(data):
        name = data['profession']  # название вакансии
        id = data['id']  # id номер вакансии
        try:
            salary_from = int(data['payment_from']) # нижний порог по зарплате, при отсутствии информации в вакансии присваивается 0
        except TypeError:
            salary_from = 0
        try:
            salary_to = int(data['payment_to']) # верхняя граница по зарплате, при отсутствии информации в вакансии присваивается 0
        except TypeError:
            salary_to = 0
        experience = data['experience']["title"] # опыт работы
        requirement = data['candidat'] # требования к соискателю
        vacancies_info = data # словарь с полной информацией по вокансии
        url = "https://www.superjob.ru/" # информация о сайте с вакансией
        instance = Vacancy(name, id, salary_from, salary_to, experience, requirement, vacancies_info, url)
        return instance


class Vacancy(InitFromHH, InitFromSJ):
    """
    Экземпляр данного класса - это вакансия, полученная с платформы HeadHunter
    Экземпляр класса инициализируется содержимым из словаря, полученного с платформы HeadHunter и
     должен иметь обязательные приватные свойства:
    '__name_vacancies' - название вакансии
    '__id' - id номер вакансии
    '__salary_from' - нижний порог по зарплате
    '__salary_to' - верхняя граница по зарплате
    '__experience' - опыт работы
    '__requirement' - требования к соискателю
    '__vacancies_info' - словарь с полной информацией по вокансии
    '__url' - информация о сайте с вакансией
    """

    __slots__ = ['__name_vacancies', '__id', '__salary_from', '__salary_to',
                 '__experience', '__requirement', '__vacancies_info', '__url']

    def __init__(self, name, id, salary_from, salary_to, experience, requirement, vacancies_info, url):
        self.__name_vacancies = name
        self.__id = id
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__experience = experience
        self.__requirement = requirement
        self.__vacancies_info = vacancies_info
        self.__url = url

    def __str__(self):
        return f"Название вакансии: {self.__name_vacancies}\n" \
               f"зарплата: от {self.__salary_from} до {self.__salary_to}\n" \
               f"опыт: {self.__experience}\n" \
               f"требования: {self.__requirement}\n" \
               f"адрес сайта: {self.__url}"

    def dict_vacancy(self):
        return {
            "name": self.__name_vacancies,
            "id": self.__id,
            "salary_from": self.__salary_from,
            "salary_to": self.__salary_to,
            "experience": self.__experience,
            "requirement": self.__requirement,
            "url": self.__url,
        }

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

    @property
    def url(self):
        return self.__url

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.__salary_to < other.__salary_to
