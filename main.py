# Иьпрт классов и модулей
from classes.super_job_api import SuperJobAPI
from classes.head_hunter_api import HeadHunterAPI
from classes.vacancy_hh import VacancyHH
from classes.vacancy_super_job import VacancySuperJob
from classes.json_saver import JSONSaver
from utils.functions import generation_vacancies, print_top_vacancies, filter_vacancies
import os

# Переменная для хранения адреса фала "vacancies.json", в который будут записаны отфильтрованые вакансии
data_vacancies = os.path.join("data", "vacancies.json")


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите название вакансии: ")
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filter_words_2 = input("Введите ключевые слова для фильтрации по требованию к вакансий: ")
    top_n = input("Введите количество вакансий для вывода в топ N, или нажмите Enter для вывода всех: ")

    # Создание списка вакансий с сайта HeadHunter (список экземпляров класса HeadHunterAPI)
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query, filter_words)
    hh_vacancies_list = generation_vacancies(hh_vacancies, VacancyHH)

    # Создание списка вакансий с сайта SuperJob (список экземпляров класса SuperJobAPI)
    superjob_api = SuperJobAPI()
    superjob_vacancies = superjob_api.get_vacancies(search_query, filter_words)
    superjob_vacancies_list = generation_vacancies(superjob_vacancies, VacancySuperJob)

    # Создание общего списка вакансий и сортировка по уровню зарплаты
    # (список экземпляров классов HeadHunterAPI и SuperJobAPI)
    vacancies_list = hh_vacancies_list + superjob_vacancies_list

    # Создание общего списка вакансий, отсоритованого по ключевому слову filter_words_2
    # и по уровню зарплаты
    filtered_vacancies_list = filter_vacancies(vacancies_list, filter_words_2)
    filtered_vacancies_list.sort(key=lambda x: x.salary_to, reverse=True)

    # Вывод ползователю список вакансий
    print_top_vacancies(filtered_vacancies_list, top_n)

    # Сохранение списка вакансий в файл vacancies.json
    json_saver = JSONSaver(filtered_vacancies_list, data_vacancies)


if __name__ == "__main__":
    user_interaction()
