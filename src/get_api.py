from abc import ABC, abstractmethod
import os
from pprint import pprint

import requests


class GetAPI(ABC):

    @abstractmethod
    def connect_to_api(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def build_universal_list_of_vacancies(self):
        pass


class HeadHunterAPI(GetAPI):

    HEADERS = {"User-Agent": "AnyApp/1.0"}
    URL = "https://api.hh.ru/vacancies"

    def __init__(self, keyword=None):
        self.params = {"text": keyword}

    def connect_to_api(self) -> object:
        result = requests.get(self.URL, params=self.params, headers=self.HEADERS)
        result_json = result.json()
        return result_json

    def get_vacancies(self):
        result_json = self.connect_to_api()
        list_of_vacancies = result_json['items']
        return list_of_vacancies  # выводит общую инфу, list_for_job - только по нужным полям #list_of_vacancies - общую

    def build_universal_list_of_vacancies(self):
        list_of_vacancies = self.get_vacancies()
        universal_list = []
        for dict_ in list_of_vacancies:
            universal_dict = {
                'profession': dict_['name'],
                'salary': dict_.get('salary'),
                'town': dict_.get('area'),
                'url': dict_['alternate_url'],
                'experience_id': dict_['experience']['id'],
                'experience_name': dict_['experience']['name'],
            }
            universal_list.append(universal_dict)
        return universal_list


class SuperJobAPI(GetAPI):

    API_KEY: str = os.getenv('SJ_API_KEY')
    HEADERS = {'X-Api-App-Id': API_KEY}
    URL = "https://api.superjob.ru/2.0/vacancies/"

    def __init__(self, keyword=None):
        self.params = {'keyword': 'python'}

    def connect_to_api(self) -> object:
        result = requests.get(self.URL, params=self.params,headers=self.HEADERS)
        result_json = result.json()
        return result_json

    def get_vacancies(self) -> list:
        result_json = self.connect_to_api()
        list_of_vacancies = result_json['objects']
        return list_of_vacancies  # выводит общую инфу, list_for_job - только по нужным полям

    def build_universal_list_of_vacancies(self):
        list_of_vacancies = self.get_vacancies()
        universal_list = []
        for dict_ in list_of_vacancies:
            universal_dict = {
                'profession': dict_['profession'],
                'salary': {'currency': dict_['currency'],
                           'from': dict_['payment_from'],
                           'to': dict_['payment_to'],
                           },
                'town': dict_['town']['title'],
                'url': dict_['link'],
                'experience_id': dict_['experience']['id'],
                'experience_name': dict_['experience']['title'],
            }
            universal_list.append(universal_dict)
        return universal_list


# ex1 = SuperJobAPI()
# # pprint(ex1.get_vacancies())
# pprint(ex1.build_universal_list_of_vacancies())

# ex2 = HeadHunterAPI()
# # pprint(ex2.get_vacancies())
# pprint(ex2.build_universal_list_of_vacancies())
