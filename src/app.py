import argparse

from src.controller import ParserController


class App(object):
    # Główna klasa aplikacji, pobiera jako argument ścieżkę do pliku z logami
    def __init__(self):
        arguments_parser = argparse.ArgumentParser()
        arguments_parser.add_argument('file')
        self._file = arguments_parser.parse_args().file

    def run(self):
        # Wypisuje na ekranie widok zwrócony przez kontroler
        print(ParserController.parse_action(self._file))
