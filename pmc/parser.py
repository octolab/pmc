from abc import ABCMeta, abstractmethod
from yaml import load
from yaml.scanner import ScannerError


class Parser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(self, _file):
        """
        :param file _file:

        :return: dict

        :raises ParseError:
        """
        pass

    @abstractmethod
    def validate(self, _file):
        """
        :param file _file:

        :raises ValidateError:
        """
        pass


class YamlParser(Parser):
    def parse(self, _file):
        try:
            return dict(load(open(_file).read()))
        except ScannerError:
            raise ParseError(ScannerError)

    def validate(self, _file):
        pass


class ParseError(SyntaxError):
    __source_error = None

    def __init__(self, source_error):
        """
        :param Exception source_error:
        """
        self.__source_error = source_error

    def get_source_error(self):
        """
        :return: Exception
        """
        return self.__source_error


class ValidateError(SyntaxError):
    pass
