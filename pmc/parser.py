from abc import ABCMeta, abstractmethod
import yaml


class Parser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(self, _file):
        """
        :param file _file:

        :return dict
        """
        pass


class YamlParser(Parser):
    def parse(self, _file):
        return dict(yaml.load(open(_file).read()))
