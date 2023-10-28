from abc import ABC, abstractmethod
import os
from pprint import pprint

import requests

api_key: str = os.getenv('SJ_API_KEY')

list_of_params_sj = {
    'keyword': 'python',
    'town': 'Москва'
}

list_of_params_hh = {
    'word': 'python',
    'town': 'Москва'
}

headers_for_sj = {
    'X-Api-App-Id': api_key,
}


class GetAPI(ABC):

    @abstractmethod
    def connect_to_api(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(GetAPI):

    def connect_to_api(self):
        result = requests.get("https://api.hh.ru/vacancies/?", params=list_of_params_hh)
        result_json = result.json()
        return result_json

    def get_vacancies(self):
        result_json = HeadHunterAPI.connect_to_api(self)
        list_of_vacancies = result_json['items']
        # num_index = 0
        # list_for_job = []
        # for vacancy in list_of_vacancies:
        #     dict_vacancy = {
        #         'profession': list_of_vacancies[num_index]['name'],
        #         #'payment_from': list_of_vacancies[num_index]['salary']['from'],
        #         #'payment_to': list_of_vacancies[num_index]['salary']['to'],
        #         'town': list_of_vacancies[num_index]['area']['name'],
        #         'link': list_of_vacancies[num_index]['alternate_url'],
        #         'experience-id': list_of_vacancies[num_index]['experience']['id'],
        #         'experience-title': list_of_vacancies[num_index]['experience']['name'],
        #     }
        #     list_for_job.append(dict_vacancy)
        #     num_index += 1
        return list_of_vacancies  # выводит общую инфу, list_for_job - только по нужным полям #list_of_vacancies - общую


class SuperJobAPI(GetAPI):

    def connect_to_api(self):
        result = requests.get("https://api.superjob.ru/2.0/vacancies/?", params=list_of_params_sj, headers=headers_for_sj)
        result_json = result.json()
        return result_json

    def get_vacancies(self):
        result_json = SuperJobAPI.connect_to_api(self)
        list_of_vacancies = result_json['objects']
        # num_index = 0
        # list_for_job = []
        # for vacancy in list_of_vacancies:
        #     dict_vacancy = {
        #         'profession': list_of_vacancies[num_index]['profession'],
        #         'payment_from': list_of_vacancies[num_index]['payment_from'],
        #         'payment_to': list_of_vacancies[num_index]['payment_to'],
        #         'town': list_of_vacancies[num_index]['town']['title'],
        #         'link': list_of_vacancies[num_index]['link'],
        #         'experience-id': list_of_vacancies[num_index]['experience']['id'],
        #         'experience-title': list_of_vacancies[num_index]['experience']['title'],
        #     }
        #     list_for_job.append(dict_vacancy)
        #     num_index += 1
        return list_of_vacancies #выводит общую инфу, list_for_job - только по нужным полям


#ex1 = SuperJobAPI()
#pprint(ex1.get_vacancies())

ex2 = HeadHunterAPI()
pprint(ex2.get_vacancies())