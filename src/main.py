from src.job_vacancies import JobVacancies
from src.job_vacancies import instantiation_hh, instantiation_sj
from src.saver import JsonSaver
from pprint import pprint


def collect_data(platform, keyword):
    """Передаёт информацию для поиска"""
    if platform == 1:
        instantiation_hh(keyword)
    elif platform == 2:
        instantiation_sj(keyword)
    elif platform == 3:
        instantiation_hh(keyword)
        instantiation_sj(keyword)
    else:
        print('Не понял ваш ответ, подготовил выборку вакансий со всех сайтов.')
        instantiation_hh(keyword)
        instantiation_sj(keyword)


def sort_by_experience(data, experience):
    """Сортировка вакансий по наличию опыта"""
    if experience == 1:
        for dict_ in data:
            if dict_.experience_id == 1:
                print(dict_)
                currency_data.append(dict_)
    elif experience == 2:
        for dict_ in data:
            if dict_.experience_id == 2:
                print(dict_)
                currency_data.append(dict_)
    elif experience == 3:
        for dict_ in data:
            if dict_.experience_id == 3:
                print(dict_)
                currency_data.append(dict_)
    elif experience == 4:
        for dict_ in data:
            if dict_.experience_id == 4:
                print(dict_)
                currency_data.append(dict_)
    else:
        print('Данные не указаны, подберём вакансии, не требующие опыта работы')
        for dict_ in data:
            if dict_.experience_id == 1:
                print(dict_)
                currency_data.append(dict_)


def sort_by_town(data, town):
    """Сортировка по городу"""
    for dict_ in data:
        if dict_.town == town:
            print(dict_)
            currency_data.append(dict_)


def sort_by_salary(data):
    """Сортировка по зарплате"""
    print('Сколько вакансий вывести на экран?')
    count_vac = int(input())
    if count_vac >= len(data):
        count_vac = len(data)
    data = sorted(data)
    for dict_ in data[-count_vac:]:
        pprint(dict_)
        currency_data.append(dict_)


def choose_method_sort(data, choose_sort):
    """Обработка ответа пользователя по выбору сортировки"""
    if choose_sort == 1:
        print('Напишите цифру, которая соответствует вашему опыту работы:')
        print("1 - Нет опыта\n2 - От 1 года до 3 лет\n3 - От 3 до 6 лет\n4 - Более 6 лет")
        experience = int(input())
        sort_by_experience(data, experience)
    elif choose_sort == 2:
        print('Введите город, в котором ищем работу')
        town = input()
        sort_by_town(data, town)
    elif choose_sort == 3:
        sort_by_salary(data)
    else:
        for dict_ in data:
            pprint(dict_)
            currency_data.append(dict_)


if __name__ == '__main__':
    while True:
        """Получение данных для запроса"""
        print('Приветствую! Я умею искать вакансии на сайтах HeadHunter и SuperJob.')
        print('Выбери цифру, на каком ресурсе начнём искать новую работу.')
        print('1 - HH\n2 - SJ\n3 - HH и SJ')
        platform = int(input())
        print('Введите ключевое слово для поиска (например, python):')
        keyword = (input()).lower().replace(" ", "")

        """Инициализация запроса"""
        collect_data(platform, keyword)
        data = JobVacancies.current_vacancies.copy()
        currency_data = []

        """Выбор параметров для сортировки"""
        print(f'По какому критерию сортировать вакансии?')
        print('1 - с учётом опыта\n2 - с учётом города\n3 - сортировать по зарплате')
        choose_sort = int(input())

        """Запуск сортировки и вывод результата на экран"""
        choose_method_sort(data, choose_sort)

        """Сохранить и выйти/Начать подбор заново"""
        print(f"\nЕсли результат поиска тебя устроил, напиши 'yes', и я сохраню подобранные вакансии в файл.")
        print("Если хочешь пройти выборку вакансий ещё раз, нажми enter, и мы продолжим поиски :)")
        save_or_repeat = input()
        if save_or_repeat == 'yes':
            print("Напиши название для сохранения файла")
            filename = input()
            saver = JsonSaver()
            saver.save_vacancies_to_file(currency_data, filename)
            print(f"Сохранил подборку вакансий в файл {filename}")
            print('Нажми 1 - чтобы посмотреть сохранённые вакансии, 2 - чтобы удалить файл')
            answer = int(input())
            if answer == 1:
                data_json = saver.show_saved_vacancies(filename)
                print(data_json)
            elif answer == 2:
                saver.remove_file(filename)
                print(f'{filename} удалён')
            break
        else:
            print("Попробуем ещё раз ;)")
            continue
    print("Удачи на собеседовании :)")
