class Row(object):
    def __init__(self, key, value):
        self._key = key
        self._value = value

    def get_key(self):
        return self._key

    def get_value(self):
        return self._value


class Result(object):
    def __init__(self, title: str):
        self._title = title
        self._rows = []

    def add_row(self, row: Row):
        self._rows.append(row)

    def get_title(self):
        return self._title

    def get_rows(self):
        return self._rows


class Log(object):
    def __init__(self, level: str, file: str, line: int, code: int):
        self._level = level
        self._file = file
        self._line = line
        self._code = code

    def get_error_level(self):
        return self._level

    def get_file(self):
        return self._file

    def get_line(self):
        return self._line

    def get_code(self):
        return self._code
