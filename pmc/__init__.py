"""
    pmc
    ~~~

    Simple package metadata compiler. You can use it with package.meta to describe your composer, npm, etc. packages.

    :copyright: (c) 2013-2016 OctoLab, https://www.octolab.org/ <feedback@octolab.org>
    :license: MIT
"""

from .filesystem import File, Watcher
from .parser import Parser, YamlParser, ParseError, ValidateError
from .processor import Processor, ComposerProcessor

__all__ = [
    'File', 'Watcher',
    'Parser', 'YamlParser', 'ParseError', 'ValidateError',
    'Processor', 'ComposerProcessor',
]
__version__ = '1.0.0'
