import json
import csv


class Saver:
    """
    Класс для сохраненеия списка отфильтрованных пользователем вакансий в файл
    """

    def __init__(self, vacancies_list):
        self.vacancies_list = list(map(lambda x: x.dict_vacancy(), vacancies_list))

    def vacancies_json(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(self.vacancies_list, file, ensure_ascii=False)

    def vacancies_csv(self, file_name):
        with open(file_name, 'w', newline="") as csvfile:
            fieldnames = ['name', 'id', 'salary_from', 'salary_to',
                          'experience', 'requirement', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.vacancies_list)
