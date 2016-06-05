from abc import ABCMeta, abstractmethod, abstractproperty
import json


class Processor(object):
    __metaclass__ = ABCMeta
    __registry = {}

    @classmethod
    def get_registered_processors(cls):
        """
        :return: dict
        """
        return cls.__registry

    @classmethod
    def register(cls):
        processor = cls()
        cls.__registry[processor.get_id()] = processor

    @abstractproperty
    def get_filename(self):
        """
        :return: str
        """
        pass

    @abstractproperty
    def get_id(self):
        """
        :return: str
        """
        pass

    @abstractmethod
    def process(self, content):
        """
        :param dict content:

        :return: str
        """
        pass


class ComposerProcessor(Processor):
    def get_id(self):
        return 'composer'

    def get_filename(self):
        return 'composer.json'

    def process(self, content):
        return json.dumps(content, indent=2)


ComposerProcessor.register()
