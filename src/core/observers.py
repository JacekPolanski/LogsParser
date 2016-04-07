import operator

from abc import ABCMeta, abstractmethod
from src.entity import Result, Row, Log


class Observer(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._dictionary = {}

    @abstractmethod
    def update(self, log: Log):
        pass

    @abstractmethod
    def get_result(self):
        pass

    def get_sorted_dictionary_by_key_asc(self):
        return sorted(self._dictionary.items(), key=operator.itemgetter(0))

    def get_sorted_dictionary_by_value_desc(self):
        return sorted(self._dictionary.items(), key=operator.itemgetter(1), reverse=True)

    def add_values_to_dictionary(self, value):
        if value in self._dictionary:
            self._dictionary[value] += 1
        else:
            self._dictionary[value] = 0


class ErrorsCounter(Observer):
    def get_result(self):
        result = Result('Liczba błędów według poziomu')
        for key, value in self.get_sorted_dictionary_by_key_asc():
            result.add_row(Row(key, value))

        return result

    def update(self, log: Log):
        self.add_values_to_dictionary(log.get_error_level())


class CodesCounter(Observer):
    def get_result(self):
        result = Result('Top 5 najczęściej występujących kodów błędów:')
        for key, value in self.get_sorted_dictionary_by_value_desc()[0:5]:
            result.add_row(Row('kod {0}'.format(key), value))

        return result

    def update(self, log: Log):
        self.add_values_to_dictionary(log.get_code())


class FilesCounter(Observer):
    def get_result(self):
        result = Result('TOP 5 najczęściej występujących plików:')
        for key, value in self.get_sorted_dictionary_by_value_desc()[0:5]:
            result.add_row(Row('pliki {0}'.format(key), value))

        return result

    def update(self, log: Log):
        self.add_values_to_dictionary(log.get_file())
