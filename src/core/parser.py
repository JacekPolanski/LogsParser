from xml.dom import minidom

from src.core.observers import ErrorsCounter, CodesCounter, FilesCounter
from src.entity import Log
from src.core.observable import Observable


class Parser(object):
    # Parser logów
    def __init__(self):
        # Deklaracja i rejestracja obserwatorów
        self._observers = Observable()
        self._observers.register(ErrorsCounter())
        self._observers.register(CodesCounter())
        self._observers.register(FilesCounter())

    def parse(self, file: str):
        for log in minidom.parse(file).childNodes[0].getElementsByTagName("log"):
            # Event, którego nasłuchują obserwatorzy
            self._observers.update(Log(
                log.getElementsByTagName("level")[0].childNodes[0].nodeValue,
                log.getElementsByTagName("file")[0].childNodes[0].nodeValue,
                int(log.getElementsByTagName("line")[0].childNodes[0].nodeValue),
                int(log.getElementsByTagName("code")[0].childNodes[0].nodeValue)
            ))

    def get_observers(self):
        # Zwraca obserwatorów
        return self._observers
