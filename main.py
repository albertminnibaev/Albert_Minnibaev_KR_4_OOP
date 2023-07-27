# Импорт классов и модулей
from classes.super_job_api import SuperJobAPI
from classes.head_hunter_api import HeadHunterAPI
from classes.saver import Saver
from utils.functions import print_top_vacancies, filter_vacancies
from classes.vacancy import Vacancy
import os

# Переменная для хранения адреса файлов "vacancies.json" и "vacancies.csv",
# в которые будут записаны отфильтрованые вакансии
vacancies_json = os.path.join("data", "vacancies.json")
vacancies_csv = os.path.join("data", "vacancies.csv")


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите название вакансии: ")
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filter_words_2 = input("Введите ключевые слова для фильтрации по требованию к вакансий: ")
    top_n = input("Введите количество вакансий для вывода в топ N, или нажмите Enter для вывода всех: ")

    # Создание списка вакансий с сайта HeadHunter (список экземпляров класса Vacancy)
    hh_api = HeadHunterAPI()
    data_from_hh = hh_api.get_vacancies(search_query, filter_words)
    hh_vacancies_list = [Vacancy.init_from_hh_dict(item) for item in data_from_hh[list(data_from_hh.keys())[0]]]

    # Создание списка вакансий с сайта SuperJob (список экземпляров класса Vacancy)
    superjob_api = SuperJobAPI()
    data_from_sj = superjob_api.get_vacancies(search_query, filter_words)
    superjob_vacancies_list = [Vacancy.init_from_sj_dict(item) for item in data_from_sj[list(data_from_sj.keys())[0]]]

    # Создание общего списка вакансий, отсоритованого по ключевому слову filter_words_2
    # и по уровню зарплаты
    vacancies_list = hh_vacancies_list + superjob_vacancies_list
    filtered_vacancies_list = filter_vacancies(vacancies_list, filter_words_2)
    filtered_vacancies_list.sort(key=lambda x: x.salary_to, reverse=True)

    # Вывод ползователю список вакансий
    print_top_vacancies(filtered_vacancies_list, top_n)

    # Сохранение списка вакансий в файлы "vacancies.json" и "vacancies.csv"
    saver = Saver(filtered_vacancies_list)
    saver.vacancies_json(vacancies_json)
    saver.vacancies_csv(vacancies_csv)


if __name__ == "__main__":
    user_interaction()
