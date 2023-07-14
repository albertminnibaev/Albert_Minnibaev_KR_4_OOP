import json


class JSONSaver:
    """
    Класс для сохраненеия списка отфильтрованных пользователем вакансий в файл
    """

    def __init__(self, vacancies_list, file_name):
        self.vacancies_list = list(map(lambda x: x.vacancies_info, vacancies_list))
        self.file_name = file_name
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(self.vacancies_list, file, ensure_ascii=False)