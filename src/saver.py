import json
import os
from abc import ABC, abstractmethod


class Saver(ABC):

    @abstractmethod
    def save_vacancies_to_file(self, currency_data, filename):
        pass

    @abstractmethod
    def show_saved_vacancies(self, filename):
        pass

    @abstractmethod
    def remove_file(self, filename):
        pass


class JsonSaver(Saver):

    def save_vacancies_to_file(self, currency_data, filename):
        list_to_save = []
        with open(filename, 'w', encoding='utf-8') as file:
            for dict_ in currency_data:
                list_to_save.append(json.dumps(str(dict_), ensure_ascii=False))
            file.write(json.dumps(list_to_save, ensure_ascii=False, indent=4))

    def show_saved_vacancies(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return json_data

    def remove_file(self, filename):
        os.remove(filename)
