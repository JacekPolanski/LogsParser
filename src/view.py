from src.entity import Result


class View(object):
    def __init__(self, result: Result):
        self._result = result

    def render(self):
        view = '------------------------------------------------\n' \
               '{0}\n' \
               '------------------------------------------------\n'\
            .format(self._result.get_title())

        for row in self._result.get_rows():
            view += '{0} - {1}\n'.format(row.get_key(), row.get_value())
        view += '------------------------------------------------\n'

        return view
