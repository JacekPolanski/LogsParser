from src.entity import Log
from src.view import View


class Observable(object):
    def __init__(self):
        self._observers = []

    def register(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def update(self, log: Log):
        for observer in self._observers:
            observer.update(log)

    def render(self):
        views_string = ''
        for observer in self._observers:
            views_string += View(observer.get_result()).render()

        return views_string
