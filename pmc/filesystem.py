import hashlib
import time

from os import getcwd, path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from .parser import ParseError


class File(object):
    __abs = None

    def __init__(self, filename):
        """
        :param str filename:
        """
        self.__abs = filename if path.isabs(filename) else path.join(getcwd(), filename)

    def get_absolute_path(self):
        """
        :return: str
        """
        return self.__abs

    def get_containing_dir(self):
        """
        :return: str
        """
        return path.dirname(self.__abs)

    def get_name(self):
        """
        :return: str
        """
        return path.basename(self.__abs)

    def get_new_name(self, filename):
        """
        :param str filename:
        :return: str
        """
        return path.join(self.get_containing_dir(), filename)


class Watcher(FileSystemEventHandler):
    @classmethod
    def watch(cls, filename, callback, recursive=False):
        """
        :param str filename:
        :param callback:
        :param bool recursive:
        """
        f = File(filename)
        observer = Observer()
        observer.schedule(cls(f, callback), f.get_containing_dir(), recursive=recursive)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    __callback = None
    __checksum = None
    __file = None

    def __init__(self, _file, callback):
        """
        :param File _file:
        :param function callback:
        """
        self.__callback = callback
        self.__file = _file
        self.__checksum = self.__calc_checksum()

    def on_modified(self, event):
        """
        :param watchdog.events.FileSystemEvent event:
        """
        # unfortunately event.is_directory is always true and event.src_path does not contain File.get_absolute_path()
        before = self.__checksum
        after = self.__calc_checksum()
        if before != after:
            try:
                self.__callback()
            except ParseError:
                pass
            self.__checksum = after

    def __calc_checksum(self):
        """
        :return: str
        """
        return hashlib.md5(open(self.__file.get_absolute_path(), 'rb').read()).hexdigest()
