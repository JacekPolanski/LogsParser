from src.core.parser import Parser


class ParserController(object):
    # Wywołuje parsowanie pliku i zwraca gotowy widok
    @staticmethod
    def parse_action(file: str):
        parser = Parser()
        parser.parse(file)

        return parser.get_observers().render()
