from get_api import HeadHunterAPI, SuperJobAPI
from pprint import pprint


class JobVacancies:

    current_vacancies = []

    def __init__(self, profession: str, salary: dict, town: dict, url: str, experience_id, experience_name):
        self.profession = profession
        self.town = town
        self.url = url
        self.experience_name = experience_name

        if self.experience_name == "Нет опыта" or self.experience_name == "без опыта":
            self.experience_name = "без опыта"
            self.experience_id = 1
        elif self.experience_name == "От 1 года до 3 лет" or self.experience_name == "От 1 года":
            self.experience_name = "опыт работы от 1 года до 3 лет"
            self.experience_id = 2
        elif self.experience_name == "От 3 до 6 лет" or self.experience_name == "От 3 лет":
            self.experience_name = "опыт работы от 3 до 6 лет"
            self.experience_id = 3
        elif self.experience_name == "Более 6 лет" or self.experience_name == "От 6 лет":
            self.experience_name = "опыт работы более 6 лет"
            self.experience_id = 4
        else:
            self.experience_name = "опыт работы не требуется"
            self.experience_id = 55

        if not salary:
            self.salary_from = 0
            self.salary_to = 0
            self.salary_currency = None
        else:
            self.salary_from = salary.get('from')
            self.salary_to = salary.get('to')
            self.salary_currency = salary.get('currency')

        self.current_vacancies.append(self)

    def __str__(self):
        if self.salary_from == 0 or self.salary_from is None:
            optional_from = ''
        else:
            optional_from = f" от {self.salary_from}"

        if self.salary_to == 0 or self.salary_to is None:
            optional_to = ''
        else:
            optional_to = f" до {self.salary_to}"

        if self.salary_currency is None:
            optional_currency = 'не указана'
        else:
            optional_currency = self.salary_currency

        return (f"{self.profession}, зарплата{optional_from}{optional_to} {optional_currency}, "
                f"{self.experience_name}, местоположение {self.town}, {self.url}")

    def __gt__(self, other):
        """Сравнение по минимальной зарплате"""
        if self.salary_from is None:
            self.salary_from = 0
        elif other.salary_from is None:
            other.salary_from = 0
        return self.salary_from > other.salary_from


def instantiation_hh(keyword):
    """Создание экземпляров класса JobVacancies от НН"""
    hh = HeadHunterAPI(keyword)
    universal_list = hh.build_universal_list_of_vacancies()
    for dict_ in universal_list:
        JobVacancies(dict_['profession'], dict_['salary'], dict_['town'], dict_['url'], dict_['experience_id'],
                     dict_['experience_name'])

def instantiation_sj(keyword):
    """Создание экземпляров класса JobVacancies от SJ"""
    sj = SuperJobAPI(keyword)
    universal_list = sj.build_universal_list_of_vacancies()
    for dict_ in universal_list:
        JobVacancies(dict_['profession'], dict_['salary'], dict_['town'], dict_['url'], dict_['experience_id'],
                     dict_['experience_name'])
