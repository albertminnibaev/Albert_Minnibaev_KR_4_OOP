def print_top_vacancies(vacancies_list, top_count):
    """
    Выводит в консоль для пользователя список Top вакансий
    :param vacancies_list: список вакансий
    :param top_count: количество вакансий для вывода
    :return: список Top вакансий
    """
    if vacancies_list:
        try:
            int(top_count)
        except ValueError:
            for i in range(len(vacancies_list)):
                print(f"Вакансия №{i + 1}")
                print(vacancies_list[i])
                print("\n")
        else:
            for i in range(int(top_count)):
                print(f"Вакансия №{i + 1}")
                print(vacancies_list[i])
                print("\n")
    else:
        print("Нет вакансий, соответствующих заданным критериям.")


def filter_vacancies(vacancies_list, filter_words):
    """
    :param vacancies_list: список вакансий
    :param filter_words: ключевое слово для фильтрации
    :return: отфильтрованный список вакансий
    """
    filtered_vacancies_list = []
    for i in range(len(vacancies_list)):
        if filter_words in str(vacancies_list[i].requirement):
            filtered_vacancies_list.append(vacancies_list[i])
    return filtered_vacancies_list
